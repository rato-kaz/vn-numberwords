"""Core primitives: interfaces, transformer, utils"""

from .interfaces import DictionaryInterface
from .transformer import NumberTransformer
from .utils import parse_vietnamese_number, format_number_with_dots

__all__ = [
    "DictionaryInterface",
    "NumberTransformer",
    "parse_vietnamese_number",
    "format_number_with_dots",
]


