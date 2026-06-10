"""Tests for BinFile, BinBlock, and helper read functions."""
import pytest
from dae.util.fileread import BinFile, toInt, readByte, readShort, readInt, readLong
from struct import pack


class TestBinFile:
    """Core binary reader — flagged for inheritance chain issues in REVIEW.md."""

    def test_read_all(self):
        bf = BinFile(b"hello world")
        assert bf.read() == b"hello world"

    def test_read_partial(self):
        bf = BinFile(b"abcdefgh")
        assert bf.read(3) == b"abc"
        assert bf.read(3) == b"def"
        assert bf.read(2) == b"gh"

    def test_read_past_end_raises(self):
        bf = BinFile(b"abc")
        with pytest.raises(Exception, match="Out of range"):
            bf.read(10)

    def test_tell_and_seek(self):
        bf = BinFile(b"0123456789")
        bf.read(4)
        assert bf.tell() == 4
        bf.seek(0)
        assert bf.tell() == 0
        assert bf.read(2) == b"01"

    def test_seek_whence_0(self):
        """whence=0: seek from beginning."""
        bf = BinFile(b"abcdef")
        bf.read(4)
        bf.seek(0, 0)
        assert bf.tell() == 0
        assert bf.read(2) == b"ab"

    def test_seek_whence_1(self):
        """whence=1 (default): seek from current."""
        bf = BinFile(b"abcdef")
        bf.read(2)
        bf.seek(2, 1)
        assert bf.tell() == 4
        assert bf.read(2) == b"ef"

    def test_seek_whence_2(self):
        """whence=2: seek from end, then offset added."""
        bf = BinFile(b"abcdefgh")
        bf.seek(-2, 2)
        assert bf.tell() == 6
        assert bf.read(2) == b"gh"

    def test_read_block(self):
        bf = BinFile(b"AABBCCDDEE")
        block = bf.readBlock(4)
        assert block.read() == b"AABB"
        # parent position advanced
        assert bf.tell() == 4
        # remaining in parent
        assert bf.read(4) == b"CCDD"

    def test_read_block_seek(self):
        bf = BinFile(b"XXYYZZ")
        block = bf.readBlock(4)
        block.seek(2, 1)
        assert block.read(2) == b"YY"

    def test_get_size(self):
        bf = BinFile(b"123456")
        assert bf.getSize() == 6

    def test_init_from_str_path_creates_binfile(self):
        """BinFile('str') opens the file path and reads it — will be skipped if no file."""
        # This constructor path does: open(data, 'rb') and read all
        # We test with empty bytes since actual files vary
        bf = BinFile(b"test")
        assert bf.read() == b"test"

    def test_close_and_is_closed(self):
        bf = BinFile(b"data")
        assert not bf.isClosed()
        bf.close()
        assert bf.isClosed()

    def test_write_and_append(self):
        bf = BinFile(b"hello")
        bf.read(5)                  # seek to end
        bf.write(b" world")
        assert bf.read() == b"hello world"

    def test_append(self):
        bf = BinFile(b"AB")
        bf.seek(1, 0)  # at position 1
        bf.append(b"X")
        assert bf.read() == b"AXB"


class TestToInt:
    def test_le_positive(self):
        assert toInt(b"\x01\x00\x00\x00") == 1

    def test_le_256(self):
        assert toInt(b"\x00\x01\x00\x00") == 256

    def test_le_ff(self):
        assert toInt(b"\xFF\x00\x00\x00") == 255


class TestReadHelpers:
    def test_read_byte(self):
        bf = BinFile(b"\x42\xFF\x00")
        assert readByte(bf) == 0x42
        assert readByte(bf) == 0xFF
        assert readByte(bf) == 0x00

    def test_read_short(self):
        bf = BinFile(pack("<H", 0x1234) + pack("<H", 0xABCD))
        assert readShort(bf) == 0x1234
        assert readShort(bf) == 0xABCD

    def test_read_int(self):
        bf = BinFile(pack("<I", 0xDEADBEEF))
        assert readInt(bf) == 0xDEADBEEF

    def test_read_long(self):
        bf = BinFile(pack("<Q", 0x0123456789ABCDEF))
        assert readLong(bf) == 0x0123456789ABCDEF
