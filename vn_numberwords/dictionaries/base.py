from ..core.interfaces import DictionaryInterface
from ..exceptions import DictionaryError


class Dictionary(DictionaryInterface):
    TRIPLET_UNITS = [
        "không",
        "một",
        "hai",
        "ba",
        "bốn",
        "năm",
        "sáu",
        "bảy",
        "tám",
        "chín",
    ]

    TRIPLET_TENS = [
        "",
        "mười",
        "hai mươi",
        "ba mươi",
        "bốn mươi",
        "năm mươi",
        "sáu mươi",
        "bảy mươi",
        "tám mươi",
        "chín mươi",
    ]

    HUNDRED = "trăm"

    EXPONENTS = [
        "",
        "nghìn",
        "triệu",
        "tỷ",
        "nghìn tỷ",
        "triệu tỷ",
    ]

    def zero(self) -> str:
        """Return the word for zero.

        Returns:
            Vietnamese word for zero ("không").
        """
        return self.TRIPLET_UNITS[0]

    def minus(self) -> str:
        """Return the word for negative numbers.

        Returns:
            Vietnamese word for negative/minus ("âm").
        """
        return "âm"

    def separator(self) -> str:
        """Return the word separator character.

        Returns:
            Character used to separate words (space).
        """
        return " "

    def triplet_ten_separator(self) -> str:
        """Return separator word when hundred is present but ten is zero.

        Returns:
            Vietnamese separator word ("linh").
        """
        return "linh"

    def special_triplet_unit_one(self) -> str:
        """Return special pronunciation for unit 1 after tens >= 2.

        Returns:
            Vietnamese word for 1 in special context ("mốt").
        """
        return "mốt"

    def special_triplet_unit_four(self) -> str:
        """Return special pronunciation for unit 4 after tens >= 2.

        Returns:
            Vietnamese word for 4 (Northern: "bốn").
        """
        return "bốn"

    def special_triplet_unit_five(self) -> str:
        """Return special pronunciation for unit 5 after tens 1-5.

        Returns:
            Vietnamese word for 5 in special context ("lăm").
        """
        return "lăm"

    def fraction(self) -> str:
        """Return the word for decimal point.

        Returns:
            Vietnamese word for decimal point ("phẩy").
        """
        return "phẩy"

    def get_triplet_unit(self, unit: int) -> str:
        """Get the word for a unit digit (0-9).

        Args:
            unit: The unit digit (0-9).

        Returns:
            Vietnamese word for the unit digit.

        Raises:
            DictionaryError: If unit is not in 0-9 range.
        """
        if not (0 <= unit <= 9):
            raise DictionaryError(f"Unit arg ({unit}) must be in 0-9 range!")
        return self.TRIPLET_UNITS[unit]

    def get_triplet_ten(self, ten: int) -> str:
        """Get the word for a tens digit (0-9).

        Args:
            ten: The tens digit (0-9).

        Returns:
            Vietnamese word for the tens digit.

        Raises:
            DictionaryError: If ten is not in 0-9 range.
        """
        if not (0 <= ten <= 9):
            raise DictionaryError(f"Ten arg ({ten}) must be in 0-9 range!")
        return self.TRIPLET_TENS[ten]

    def get_triplet_hundred(self, hundred: int) -> str:
        """Get the word for a hundreds digit (0-9).

        Args:
            hundred: The hundreds digit (0-9).

        Returns:
            Vietnamese word for the hundreds digit with "trăm".

        Raises:
            DictionaryError: If hundred is not in 0-9 range.
        """
        if not (0 <= hundred <= 9):
            raise DictionaryError(f"Hundred arg ({hundred}) must be in 0-9 range!")
        return self.TRIPLET_UNITS[hundred] + self.separator() + self.HUNDRED

    def get_exponent(self, power: int) -> str:
        """Get the word for a power of 1000 (magnitude).

        Args:
            power: The exponent (0=ones, 1=thousands, 2=millions, etc.).

        Returns:
            Vietnamese word for the magnitude.

        Raises:
            DictionaryError: If power is not supported in Vietnamese dictionary.
        """
        if not (0 <= power < len(self.EXPONENTS)):
            raise DictionaryError(f"Power arg ({power}) not exist in vietnamese dictionary!")
        return self.EXPONENTS[power]
