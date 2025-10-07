from typing import Union, List

from .dictionaries import DictionaryInterface
from core.transformer import NumberTransformer
from core.utils import parse_vietnamese_number


def number_to_words(number: Union[int, float, str], dictionary: DictionaryInterface = None) -> str:
    transformer = NumberTransformer(dictionary)
    return transformer.to_words(number)


def number_to_currency(
    number: Union[int, float, str], unit: Union[str, List[str]] = "đồng", dictionary: DictionaryInterface = None
) -> str:
    transformer = NumberTransformer(dictionary)
    return transformer.to_currency(number, unit)


def vietnamese_string_to_words(number_str: str, dictionary: DictionaryInterface = None) -> str:
    number = parse_vietnamese_number(number_str)
    return number_to_words(number, dictionary)


def vietnamese_string_to_currency(
    number_str: str, unit: Union[str, List[str]] = "đồng", dictionary: DictionaryInterface = None
) -> str:
    number = parse_vietnamese_number(number_str)
    return number_to_currency(number, unit, dictionary)


