"""Custom exceptions for vn-numberwords library."""


class VnNumberWordsError(Exception):
    """Base exception for vn-numberwords library."""

    pass


class InvalidNumberError(VnNumberWordsError):
    """Raised when input is not a valid number."""

    pass


class InvalidWordsError(VnNumberWordsError):
    """Raised when input words cannot be parsed."""

    pass


class DictionaryError(VnNumberWordsError):
    """Raised when dictionary operation fails."""

    pass
