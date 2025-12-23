from abc import ABC, abstractmethod


class DictionaryInterface(ABC):
    """Interface for Vietnamese number dictionary"""

    @abstractmethod
    def zero(self) -> str:
        """Return the word for zero.

        Returns:
            Vietnamese word for zero.
        """
        pass

    @abstractmethod
    def minus(self) -> str:
        """Return the word for negative numbers.

        Returns:
            Vietnamese word for negative/minus.
        """
        pass

    @abstractmethod
    def separator(self) -> str:
        """Return the word separator character.

        Returns:
            Character used to separate words (typically a space).
        """
        pass

    @abstractmethod
    def fraction(self) -> str:
        """Return the word for decimal point.

        Returns:
            Vietnamese word for decimal point/fraction separator.
        """
        pass

    @abstractmethod
    def special_triplet_unit_one(self) -> str:
        """Return special pronunciation for unit 1 after tens >= 2.

        Returns:
            Vietnamese word for 1 in special context (e.g., "mốt" in 21).
        """
        pass

    @abstractmethod
    def special_triplet_unit_four(self) -> str:
        """Return special pronunciation for unit 4 after tens >= 2.

        Returns:
            Vietnamese word for 4 in special context (Northern vs Southern).
        """
        pass

    @abstractmethod
    def special_triplet_unit_five(self) -> str:
        """Return special pronunciation for unit 5 after tens 1-5.

        Returns:
            Vietnamese word for 5 in special context (e.g., "lăm" in 25).
        """
        pass

    @abstractmethod
    def triplet_ten_separator(self) -> str:
        """Return separator word when hundred is present but ten is zero.

        Returns:
            Vietnamese word for separator (e.g., "linh" or "lẻ").
        """
        pass

    @abstractmethod
    def get_triplet_unit(self, unit: int) -> str:
        """Get the word for a unit digit (0-9).

        Args:
            unit: The unit digit (0-9).

        Returns:
            Vietnamese word for the unit digit.
        """
        pass

    @abstractmethod
    def get_triplet_ten(self, ten: int) -> str:
        """Get the word for a tens digit (0-9).

        Args:
            ten: The tens digit (0-9).

        Returns:
            Vietnamese word for the tens digit.
        """
        pass

    @abstractmethod
    def get_triplet_hundred(self, hundred: int) -> str:
        """Get the word for a hundreds digit (0-9).

        Args:
            hundred: The hundreds digit (0-9).

        Returns:
            Vietnamese word for the hundreds digit with "trăm".
        """
        pass

    @abstractmethod
    def get_exponent(self, power: int) -> str:
        """Get the word for a power of 1000 (magnitude).

        Args:
            power: The exponent (0=ones, 1=thousands, 2=millions, etc.).

        Returns:
            Vietnamese word for the magnitude (e.g., "nghìn", "triệu", "tỷ").
        """
        pass
