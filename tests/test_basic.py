from vn_numberwords import (
    number_to_words,
    number_to_currency,
    vietnamese_string_to_words,
    Dictionary,
    SouthDictionary,
)


def test_number_to_words_basic():
    assert number_to_words(0) == "không"
    assert number_to_words(10) == "mười"
    assert number_to_words(21) == "hai mươi mốt"


def test_number_to_words_south():
    assert number_to_words(24, SouthDictionary()) == "hai mươi bốn"


def test_currency_and_parse():
    assert number_to_currency(1234, "đồng") == "một nghìn hai trăm linh bốn đồng"
    assert (
        vietnamese_string_to_words("1.234")
        == "một nghìn hai trăm ba mươi tư"
    )


def test_plain_integer_input():
    # Integer without dots
    assert (
        number_to_words(123123)
        == "một trăm hai mươi ba nghìn một trăm hai mươi ba"
    )


def test_plain_string_input():
    # String without dots
    assert (
        vietnamese_string_to_words("123123")
        == "một trăm hai mươi ba nghìn một trăm hai mươi ba"
    )

