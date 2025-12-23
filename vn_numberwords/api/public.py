from typing import Union, List, Optional

from ..core.interfaces import DictionaryInterface
from ..core.transformer import NumberTransformer
from ..core.word_parser import WordToNumberParser
from ..core.utils import parse_vietnamese_number


def number_to_words(
    number: Union[int, float, str], dictionary: Optional[DictionaryInterface] = None
) -> str:
    """Convert a number to Vietnamese words.

    Supports integers, floats, negative numbers, and large numbers up to
    trillions. Decimal parts are read digit by digit after "phẩy".

    Args:
        number: The number to convert. Can be int, float, or string.
        dictionary: Optional custom dictionary for Vietnamese variants
            (e.g., SouthDictionary for Southern Vietnamese).

    Returns:
        Vietnamese words representation of the number.

    Raises:
        InvalidNumberError: If the input is not a valid number.

    Examples:
        >>> number_to_words(123)
        'một trăm hai mươi ba'
        >>> number_to_words(1.5)
        'một phẩy năm'
        >>> number_to_words(-5)
        'âm năm'
        >>> number_to_words(1000000)
        'một triệu'
    """
    transformer = NumberTransformer(dictionary)
    return transformer.to_words(number)


def number_to_currency(
    number: Union[int, float, str],
    unit: Union[str, List[str]] = "đồng",
    dictionary: Optional[DictionaryInterface] = None,
) -> str:
    """Convert a number to Vietnamese currency words.

    Supports both integer and decimal currency amounts. For decimal amounts,
    you can provide separate units for the main and decimal parts.

    Args:
        number: The currency amount to convert.
        unit: Currency unit(s). Can be a single string (e.g., "đồng") or
            a list of [main_unit, decimal_unit] (e.g., ["đô la", "xu"]).
        dictionary: Optional custom dictionary for Vietnamese variants.

    Returns:
        Vietnamese words representation of the currency amount.

    Raises:
        InvalidNumberError: If the input is not a valid number.

    Examples:
        >>> number_to_currency(1234, "đồng")
        'một nghìn hai trăm ba mươi bốn đồng'
        >>> number_to_currency(1.50, ["đô la", "xu"])
        'một đô la năm mươi xu'
        >>> number_to_currency(100, "USD")
        'một trăm USD'
    """
    transformer = NumberTransformer(dictionary)
    return transformer.to_currency(number, unit)


def vietnamese_string_to_words(
    number_str: str, dictionary: Optional[DictionaryInterface] = None
) -> str:
    """Convert Vietnamese-formatted number string to words.

    Parses Vietnamese number format (using dots/commas as separators)
    and converts to Vietnamese words.

    Args:
        number_str: Vietnamese-formatted number string (e.g., "1.234.567").
        dictionary: Optional custom dictionary for Vietnamese variants.

    Returns:
        Vietnamese words representation of the number.

    Raises:
        InvalidNumberError: If the input cannot be parsed as a number.

    Examples:
        >>> vietnamese_string_to_words("1.234")
        'một nghìn hai trăm ba mươi bốn'
        >>> vietnamese_string_to_words("1.234.567")
        'một triệu hai trăm ba mươi bốn nghìn năm trăm sáu mươi bảy'
    """
    number = parse_vietnamese_number(number_str)
    return number_to_words(number, dictionary)


def vietnamese_string_to_currency(
    number_str: str,
    unit: Union[str, List[str]] = "đồng",
    dictionary: Optional[DictionaryInterface] = None,
) -> str:
    """Convert Vietnamese-formatted number string to currency words.

    Parses Vietnamese number format and converts to Vietnamese currency words.

    Args:
        number_str: Vietnamese-formatted number string.
        unit: Currency unit(s). Single string or [main_unit, decimal_unit].
        dictionary: Optional custom dictionary for Vietnamese variants.

    Returns:
        Vietnamese words representation of the currency amount.

    Raises:
        InvalidNumberError: If the input cannot be parsed as a number.

    Examples:
        >>> vietnamese_string_to_currency("1.234", "đồng")
        'một nghìn hai trăm ba mươi bốn đồng'
    """
    number = parse_vietnamese_number(number_str)
    return number_to_currency(number, unit, dictionary)


def words_to_number(
    words: Union[str, List[str]], dictionary: Optional[DictionaryInterface] = None
) -> Union[int, float]:
    """Convert Vietnamese words to number.

    Supports both accented and non-accented Vietnamese text. Handles
    complex numbers with multiple magnitude keywords.

    Args:
        words: Vietnamese words as a string or list of strings.
        dictionary: Optional custom dictionary for Vietnamese variants.

    Returns:
        The numeric value as int or float.

    Raises:
        InvalidWordsError: If the words cannot be parsed.

    Examples:
        >>> words_to_number("một trăm hai mươi ba")
        123
        >>> words_to_number("mười một")
        11
        >>> words_to_number("một triệu")
        1000000
        >>> words_to_number(["hai", "mươi", "mốt"])
        21
    """
    parser = WordToNumberParser(dictionary)
    return parser.parse_words(words)


def currency_words_to_number(
    words: Union[str, List[str]],
    currency_unit: str = "đồng",
    dictionary: Optional[DictionaryInterface] = None,
) -> Union[int, float]:
    """Convert Vietnamese currency words to number.

    Parses Vietnamese currency text and extracts the numeric value.

    Args:
        words: Vietnamese currency words as string or list of strings.
        currency_unit: The currency unit to expect (e.g., "đồng", "USD").
        dictionary: Optional custom dictionary for Vietnamese variants.

    Returns:
        The numeric value as int or float.

    Raises:
        InvalidWordsError: If the words cannot be parsed.

    Examples:
        >>> currency_words_to_number("một nghìn đồng")
        1000
        >>> currency_words_to_number("năm trăm triệu đồng")
        500000000
    """
    parser = WordToNumberParser(dictionary)
    return parser.parse_currency_words(words, currency_unit)
