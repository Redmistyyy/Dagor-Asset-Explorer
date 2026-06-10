"""Tests for utility functions — formatBytes, matrixMul, vectorTransform."""
import math
import pytest
from dae.util.misc import formatBytes, matrixMul, vectorTransform


class TestFormatBytes:
    def test_bytes(self):
        assert formatBytes(0) == "0 B"
        assert formatBytes(500) == "500 B"

    def test_kb(self):
        assert formatBytes(1024) == "1 KB"
        assert formatBytes(2048) == "2 KB"
        assert formatBytes(1536) == "2 KB"  # rounds

    def test_mb(self):
        assert formatBytes(1048576) == "1 MB"
        assert formatBytes(2097152) == "2 MB"


class TestMatrixMul:
    def test_identity(self):
        I = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
        V = [[1], [2], [3]]
        assert matrixMul(I, V) == V

    def test_2x3_times_3x2(self):
        A = [[1, 2, 3], [4, 5, 6]]
        B = [[7, 8], [9, 10], [11, 12]]
        result = matrixMul(A, B)
        assert result[0][0] == 1*7 + 2*9 + 3*11   # 58
        assert result[0][1] == 1*8 + 2*10 + 3*12  # 64
        assert result[1][0] == 4*7 + 5*9 + 6*11   # 139
        assert result[1][1] == 4*8 + 5*10 + 6*12  # 154

    def test_dimension_mismatch_raises(self):
        A = [[1, 2]]      # 1x2
        B = [[1], [2], [3]]  # 3x1
        with pytest.raises(ValueError, match="dimensions"):
            matrixMul(A, B)


class TestVectorTransform:
    def test_identity(self):
        I = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0]]
        result = vectorTransform(I, [5, 10, 15])
        assert result == [5, 10, 15]

    def test_translation(self):
        T = [[1, 0, 0, 10], [0, 1, 0, 20], [0, 0, 1, 30]]
        result = vectorTransform(T, [0, 0, 0])
        assert result == [10, 20, 30]

    def test_rotation_90_z(self):
        """90° around Z: (1,0,0) → (0,1,0)."""
        Rz90 = [[0, -1, 0, 0], [1, 0, 0, 0], [0, 0, 1, 0]]
        result = vectorTransform(Rz90, [1, 0, 0])
        assert [round(v, 6) for v in result] == [0, 1, 0]
