"""Tests for LZMA compression (stdlib replacement for pylzma)."""
import pytest
from dae.util.decompression import lzmaDecompress, lzmaCompress


class TestLzma:
    """Validate that stdlib lzma replacement works for FORMAT_RAW round-trips."""

    def test_roundtrip_short(self):
        original = b"hello world " * 10
        compressed = lzmaCompress(original)
        decompressed = lzmaDecompress(compressed)
        assert decompressed == original

    def test_roundtrip_binary(self):
        original = bytes(range(256)) * 4  # 1024 bytes of binary
        compressed = lzmaCompress(original)
        decompressed = lzmaDecompress(compressed)
        assert decompressed == original

    def test_roundtrip_empty(self):
        original = b""
        compressed = lzmaCompress(original)
        decompressed = lzmaDecompress(compressed)
        assert decompressed == original

    def test_roundtrip_single_byte(self):
        original = b"\x42"
        compressed = lzmaCompress(original)
        decompressed = lzmaDecompress(compressed)
        assert decompressed == original

    def test_roundtrip_large(self):
        """~64KB to stress the codec."""
        original = (b"ABCD" * 256) * 64
        compressed = lzmaCompress(original)
        decompressed = lzmaDecompress(compressed)
        assert decompressed == original

    def test_compression_actually_reduces_size(self):
        original = b"AAAA" * 1000
        compressed = lzmaCompress(original)
        assert len(compressed) < len(original)

    def test_compress_then_decompress_standard_lzma(self):
        """Verify that the FORMAT_RAW output can be decompressed by stdlib lzma directly."""
        import lzma
        from dae.util.decompression import _LZMA_FILTERS
        original = b"test data for cross-compat check " * 50
        compressed = lzmaCompress(original)
        # stdlib lzma with FORMAT_RAW should handle our output with same filters
        decompressed = lzma.decompress(compressed, format=lzma.FORMAT_RAW, filters=_LZMA_FILTERS)
        assert decompressed == original
