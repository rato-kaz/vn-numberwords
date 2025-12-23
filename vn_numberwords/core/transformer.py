from typing import Union, List, Tuple, Optional

from .interfaces import DictionaryInterface
from ..dictionaries.base import Dictionary
from ..exceptions import InvalidNumberError


class NumberTransformer:
    """Main class for converting numbers to Vietnamese words"""

    def __init__(
        self,
        dictionary: Optional[DictionaryInterface] = None,
        decimal_part: Optional[int] = None,
    ):
        """Initialize the NumberTransformer.

        Args:
            dictionary: Custom dictionary implementation for number words.
                Defaults to the standard Vietnamese dictionary.
            decimal_part: Number of decimal places to format. If None, uses
                the natural decimal representation.

        Examples:
            >>> transformer = NumberTransformer()
            >>> transformer.to_words(123)
            'một trăm hai mươi ba'
        """
        self.dictionary = dictionary or Dictionary()
        self.decimal_part = decimal_part

    def collapse_words(self, words: List[str]) -> str:
        """Collapse a list of words into a single string using separator.

        Args:
            words: List of word strings to join together.

        Returns:
            Joined string with non-empty words separated by the dictionary separator.

        Examples:
            >>> transformer = NumberTransformer()
            >>> transformer.collapse_words(['một', '', 'hai'])
            'một hai'
        """
        separator = self.dictionary.separator()
        words = [word for word in words if word]
        return separator.join(words)

    def resolve_number(self, number: Union[int, float, str]) -> Tuple[bool, int, int]:
        """Parse and resolve a number into its components.

        Args:
            number: The number to resolve (can be int, float, or string).

        Returns:
            Tuple containing:
                - is_negative: Whether the number is negative.
                - integer_part: The integer portion of the number.
                - decimal_part: The decimal portion as an integer.

        Raises:
            InvalidNumberError: If the input is not a valid numeric value.

        Examples:
            >>> transformer = NumberTransformer()
            >>> transformer.resolve_number(123.45)
            (False, 123, 45)
            >>> transformer.resolve_number(-5)
            (True, 5, 0)
        """
        if (
            not isinstance(number, (int, float, str))
            or not str(number).replace("-", "").replace(".", "").isdigit()
        ):
            raise InvalidNumberError(f"Number arg ({number}) must be numeric!")

        if self.decimal_part is None:
            number = float(number)
            number = str(number)
        else:
            number = f"{float(number):.{self.decimal_part}f}"

        is_negative = number.startswith("-")

        if "." in number:
            parts = number.split(".", 1)
            integer_part = int(parts[0].lstrip("-"))
            decimal_part = int(parts[1])
        else:
            integer_part = int(number.lstrip("-"))
            decimal_part = 0

        return is_negative, integer_part, decimal_part

    def split_triplet(self, triplet: int) -> tuple:
        """Split a three-digit number into hundreds, tens, and units.

        Args:
            triplet: A number from 0-999.

        Returns:
            Tuple of (hundred, ten, unit) digits.

        Examples:
            >>> transformer = NumberTransformer()
            >>> transformer.split_triplet(234)
            (2, 3, 4)
        """
        hundred = (triplet // 100) % 10
        ten = (triplet // 10) % 10
        unit = triplet % 10
        return hundred, ten, unit

    def get_triplet_unit(self, unit: int, ten: int) -> str:
        """Get the word for a unit digit with special handling for context.

        Special rules apply for unit digits in certain contexts:
        - 5 after 1-5 in tens position becomes "lăm"
        - 1 after 2+ in tens position becomes "mốt"
        - 4 after 2+ in tens position can have special pronunciation

        Args:
            unit: The unit digit (0-9).
            ten: The tens digit (0-9) for context.

        Returns:
            The Vietnamese word for the unit digit in context.

        Examples:
            >>> transformer = NumberTransformer()
            >>> transformer.get_triplet_unit(5, 2)
            'lăm'
            >>> transformer.get_triplet_unit(1, 3)
            'mốt'
        """
        if 1 <= ten <= 5 and unit == 5:
            return self.dictionary.special_triplet_unit_five()

        if ten >= 2:
            if unit == 1:
                return self.dictionary.special_triplet_unit_one()
            if unit == 4:
                return self.dictionary.special_triplet_unit_four()

        return self.dictionary.get_triplet_unit(unit)

    def triplet_to_words(self, triplet: int, is_first: bool, exponent: int) -> str:
        """Convert a three-digit triplet to Vietnamese words.

        Args:
            triplet: A three-digit number (0-999).
            is_first: Whether this is the first (leftmost) triplet.
            exponent: The power of 1000 for this triplet (0=ones, 1=thousands, etc.).

        Returns:
            Vietnamese words representing the triplet with magnitude.

        Examples:
            >>> transformer = NumberTransformer()
            >>> transformer.triplet_to_words(234, True, 0)
            'hai trăm ba mươi bốn'
            >>> transformer.triplet_to_words(5, False, 1)
            'năm nghìn'
        """
        hundred, ten, unit = self.split_triplet(triplet)
        words = []

        if hundred > 0 or not is_first:
            words.append(self.dictionary.get_triplet_hundred(hundred))

            if ten == 0 and unit > 0:
                words.append(self.dictionary.triplet_ten_separator())

        if ten > 0:
            words.append(self.dictionary.get_triplet_ten(ten))

        if unit > 0:
            words.append(self.get_triplet_unit(unit, ten))

        words.append(self.dictionary.get_exponent(exponent))

        return self.collapse_words(words)

    def number_to_triplets(self, number: int) -> List[int]:
        """Convert a number into a list of three-digit triplets.

        Args:
            number: A non-negative integer.

        Returns:
            List of three-digit numbers representing triplets from right to left.

        Examples:
            >>> transformer = NumberTransformer()
            >>> transformer.number_to_triplets(1234567)
            [1, 234, 567]
        """
        triplets: List[int] = []

        while number > 0:
            triplets.insert(0, number % 1000)
            number = number // 1000

        return triplets

    def to_words(self, number: Union[int, float, str]) -> str:
        """Convert a number to Vietnamese words.

        Handles integers, floats, and negative numbers. Decimal parts are
        read digit by digit after "phẩy" (point).

        Args:
            number: The number to convert (int, float, or string).

        Returns:
            Vietnamese words representation of the number.

        Raises:
            InvalidNumberError: If the input is not a valid number.

        Examples:
            >>> transformer = NumberTransformer()
            >>> transformer.to_words(123)
            'một trăm hai mươi ba'
            >>> transformer.to_words(-5)
            'âm năm'
            >>> transformer.to_words(1.5)
            'một phẩy năm'
        """
        is_negative, integer_part, decimal_part = self.resolve_number(number)
        words = []

        if is_negative:
            words.append(self.dictionary.minus())

        if integer_part == 0:
            words.append(self.dictionary.zero())

        triplets = self.number_to_triplets(integer_part)

        for pos, triplet in enumerate(triplets):
            if triplet > 0:
                words.append(
                    self.triplet_to_words(triplet, pos == 0, len(triplets) - pos - 1)
                )

        if decimal_part > 0:
            words.append(self.dictionary.fraction())
            words.append(self.to_words(decimal_part))

        return self.collapse_words(words)

    def to_currency(
        self, number: Union[int, float, str], unit: Union[str, List[str]] = "đồng"
    ) -> str:
        """Convert a number to Vietnamese currency words.

        Args:
            number: The amount to convert (int, float, or string).
            unit: Currency unit(s). Can be a single string or list of
                [main_unit, decimal_unit] for decimal amounts.

        Returns:
            Vietnamese words representation of the currency amount.

        Raises:
            InvalidNumberError: If the input is not a valid number.

        Examples:
            >>> transformer = NumberTransformer()
            >>> transformer.to_currency(1234, "đồng")
            'một nghìn hai trăm ba mươi bốn đồng'
            >>> transformer.to_currency(1.50, ["đô la", "xu"])
            'một đô la năm mươi xu'
        """
        if isinstance(unit, str):
            unit = [unit]

        is_negative, integer_part, decimal_part = self.resolve_number(number)

        if decimal_part == 0 or len(unit) < 2:
            words = [self.to_words(number), unit[0]]
        else:
            main_unit, decimal_unit = unit[0], unit[1]
            words = []
            if is_negative:
                words.append(self.dictionary.minus())
            words.append(self.to_words(integer_part))
            words.append(main_unit)
            words.append(self.to_words(decimal_part))
            words.append(decimal_unit)

        return self.collapse_words(words)
