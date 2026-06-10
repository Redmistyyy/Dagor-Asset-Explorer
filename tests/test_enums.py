"""Tests for enums — verify constants and tag values."""
from dae.util.enums import *


class TestDialogTypes:
    def test_constants(self):
        assert DIALOG_NONE == 0
        assert DIALOG_PROGRESS == 1
        assert DIALOG_STATUS == 2
        assert DIALOG_ERROR == 3


class TestLogLevels:
    def test_constants(self):
        assert LOG_DEBUG == 0
        assert LOG_WARN == 1
        assert LOG_ERROR == 2


class TestDbldTags:
    def test_hex_values(self):
        # verify magic numbers are correct
        assert TAG_RQRL == 0x4c527152
        assert TAG_DXP2 == 0x32507844
        assert TAG_TEX == 0x58455400
        assert TAG_LMAP == 0x70616d6c
        assert TAG_HM2 == 0x324d4800
        assert TAG_RIGZ == 0x7a474952
        assert TAG_END == 0x444e4500
        assert TAG_FRT == 0x54524600


class TestSettingsKeys:
    def test_keys_are_strings(self):
        assert isinstance(SETTINGS_EXPORT_FOLDER, str)
        assert isinstance(SETTINGS_STUDIOMDL_PATH, str)
        assert isinstance(SETTINGS_EXPAND_ALL, str)


class TestMvdFlags:
    def test_constants(self):
        assert MVD_NORMAL == 0
        assert MVD_SKINNED == 1
        assert MVD_SKINNED_FLAG == 2
