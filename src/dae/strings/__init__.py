"""Localization support — lightweight dict-based i18n.

Loads translations from strings/<lang>.py at startup.
Falls back to English (the key itself) when no translation found.
"""

_TRANSLATIONS = {}
_LANG = "en"


def load_lang(lang: str):
    """Load translations for the given language code."""
    global _TRANSLATIONS, _LANG
    _LANG = lang
    if lang == "zh":
        from .zh import STRINGS
        _TRANSLATIONS = STRINGS
    else:
        _TRANSLATIONS = {}


def _(text: str) -> str:
    """Return translated string, or the original English text as fallback."""
    return _TRANSLATIONS.get(text, text)


def current_lang() -> str:
    return _LANG
