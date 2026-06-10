"""Tests for SafeRange iterators and Terminable base class."""
import pytest
from dae.util.terminable import Terminable, SafeRange, SafeEnumerate, SafeIter


class MockTerminable(Terminable):
    """Mock that doesn't trigger termination."""
    _Terminable__shouldTerminate = False


class MockTerminated(Terminable):
    """Mock that immediately signals termination."""
    _Terminable__shouldTerminate = True


class TestSafeRange:
    """Validate SafeRange — the buggy iterator flagged as P0 in REVIEW.md."""

    def test_basic_forward(self):
        parent = MockTerminable()
        vals = list(SafeRange(parent, 5))
        assert vals == [0, 1, 2, 3, 4]

    def test_start_stop(self):
        parent = MockTerminable()
        vals = list(SafeRange(parent, 2, 7))
        assert vals == [2, 3, 4, 5, 6]

    def test_start_stop_step(self):
        parent = MockTerminable()
        vals = list(SafeRange(parent, 1, 9, 2))
        assert vals == [1, 3, 5, 7]

    def test_reverse_step(self):
        parent = MockTerminable()
        vals = list(SafeRange(parent, 7, 2, -1))
        assert vals == [7, 6, 5, 4, 3]

    def test_reverse_step_single(self):
        parent = MockTerminable()
        vals = list(SafeRange(parent, 4, 3, -1))
        assert vals == [4]

    def test_reverse_empty(self):
        parent = MockTerminable()
        vals = list(SafeRange(parent, 3, 7, -1))
        assert vals == []

    def test_step_zero_raises(self):
        parent = MockTerminable()
        with pytest.raises(ValueError, match="must not be zero"):
            SafeRange(parent, 0, 5, 0)

    def test_terminated_stops_immediately(self):
        parent = MockTerminated()
        vals = list(SafeRange(parent, 100))
        assert vals == []

    def test_terminated_during_loop(self):
        """Simulate termination mid-loop by mutating the flag."""
        parent = Terminable()
        parent._Terminable__shouldTerminate = False

        result = []
        for i in SafeRange(parent, 10):
            result.append(i)
            if i == 3:
                parent._Terminable__shouldTerminate = True

        assert result == [0, 1, 2, 3]

    def test_default_args_single_stop(self):
        """SafeRange(parent, 3) → only stop given, start=0, step=1."""
        parent = MockTerminable()
        vals = list(SafeRange(parent, 3))
        assert vals == [0, 1, 2]


class TestSafeEnumerate:
    def test_basic(self):
        parent = MockTerminable()
        vals = list(SafeEnumerate(parent, ["a", "b", "c"]))
        assert vals == [(0, "a"), (1, "b"), (2, "c")]

    def test_with_start(self):
        parent = MockTerminable()
        vals = list(SafeEnumerate(parent, ["x", "y"], start=5))
        assert vals == [(5, "x"), (6, "y")]

    def test_terminated(self):
        parent = MockTerminated()
        vals = list(SafeEnumerate(parent, [1, 2, 3]))
        assert vals == []


class TestSafeIter:
    def test_basic(self):
        parent = MockTerminable()
        vals = list(SafeIter(parent, [10, 20, 30]))
        assert vals == [10, 20, 30]

    def test_terminated(self):
        parent = MockTerminated()
        vals = list(SafeIter(parent, [1, 2, 3]))
        assert vals == []
