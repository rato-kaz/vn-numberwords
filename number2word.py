"""
Vietnamese Number to Words Converter
Convert numbers to Vietnamese words
author: Nguyen Huu Vuong

Note:
- This file now serves as an executable demo/CLI entry.
- The reusable library code has been moved to the package `vn_numberwords`.
"""

# Public API is re-exported from the package to preserve compatibility
from vn_numberwords import (
    SouthDictionary,
    NumberTransformer,
    parse_vietnamese_number,
    vietnamese_string_to_words,
    vietnamese_string_to_currency,
)


# Example usage
if __name__ == "__main__":
    # Test with standard dictionary
    transformer = NumberTransformer()

    test_numbers = [
        0,
        1,
        10,
        11,
        15,
        20,
        21,
        25,
        100,
        101,
        110,
        111,
        1000,
        1001,
        1234,
        10000,
        12345,
        100000,
        1234567,
    ]

    print("=== Standard Vietnamese Dictionary ===")
    for num in test_numbers:
        print(f"{num:>8}: {transformer.to_words(num)}")

    print("\n=== Southern Vietnamese Dictionary ===")
    south_transformer = NumberTransformer(SouthDictionary())
    for num in test_numbers:
        print(f"{num:>8}: {south_transformer.to_words(num)}")

    print("\n=== Vietnamese String Input Examples ===")
    vietnamese_strings = [
        "100.034.545.435.000",
        "1.234",
        "1.000.000",
        "1.234.56",  # Decimal example
    ]

    print("Standard Dictionary:")
    for number_str in vietnamese_strings:
        try:
            parsed_number = parse_vietnamese_number(number_str)
            result = vietnamese_string_to_words(number_str)
            print(f"{number_str:>20} -> {parsed_number:>15} -> {result}")
        except Exception as e:
            print(f"{number_str:>20} -> Error: {e}")

    print("\nSouthern Dictionary:")
    for number_str in vietnamese_strings:
        try:
            parsed_number = parse_vietnamese_number(number_str)
            result = vietnamese_string_to_words(number_str, SouthDictionary())
            print(f"{number_str:>20} -> {parsed_number:>15} -> {result}")
        except Exception as e:
            print(f"{number_str:>20} -> Error: {e}")

    print("\n=== Currency Examples (Vietnamese String Input) ===")
    currency_strings = [
        "100.034.545.435.000",
        "1.234",
        "1.000.000",
    ]

    print("Standard Dictionary:")
    for number_str in currency_strings:
        try:
            parsed_number = parse_vietnamese_number(number_str)
            result = vietnamese_string_to_currency(number_str, "đồng")
            print(f"{number_str:>20} -> {parsed_number:>15} -> {result}")
        except Exception as e:
            print(f"{number_str:>20} -> Error: {e}")

    print("\nSouthern Dictionary:")
    for number_str in currency_strings:
        try:
            parsed_number = parse_vietnamese_number(number_str)
            result = vietnamese_string_to_currency(
                number_str, "đồng", SouthDictionary()
            )
            print(f"{number_str:>20} -> {parsed_number:>15} -> {result}")
        except Exception as e:
            print(f"{number_str:>20} -> Error: {e}")
