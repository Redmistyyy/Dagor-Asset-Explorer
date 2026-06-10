"""Tests for log module — basic logging functions."""
import pytest
from dae.util import log


class TestLogLevels:
    def test_initial_level(self):
        assert log.curLevel == 0

    def test_add_sub_level(self):
        before = log.curLevel
        log.addLevel()
        assert log.curLevel == before + 1
        log.subLevel()
        assert log.curLevel == before

    def test_sub_below_zero_raises(self):
        log.curLevel = 0
        with pytest.raises(Exception):
            log.subLevel()

    def test_get_level_str(self):
        log.curLevel = 0
        log.incrLevel(2)
        s = log.getLevelStr()
        assert s == "        "  # 8 spaces for level 2
        log.incrLevel(-2)  # cleanup


class TestLogOutput:
    def test_log_no_crash(self, capsys):
        """log() should not raise on valid input."""
        log.curLevel = 0
        log.log("test message")
        captured = capsys.readouterr()
        assert "test message" in captured.out

    def test_log_error(self, capsys):
        from dae.util.enums import LOG_ERROR
        log.log("error message", LOG_ERROR)
        captured = capsys.readouterr()
        assert "[E]" in captured.out
        assert "error message" in captured.out
