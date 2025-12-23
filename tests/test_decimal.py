"""Test decimal numbers, negative numbers, and edge cases."""

from vn_numberwords import number_to_words, InvalidNumberError
import pytest


def test_decimal_numbers():
    """Test decimal number conversion"""
    # Basic decimal numbers
    assert number_to_words(1.5) == "một phẩy năm"
    assert number_to_words(0.5) == "không phẩy năm"
    assert number_to_words(10.25) == "mười phẩy hai mươi lăm"

    # More complex decimals
    assert number_to_words(123.45) == "một trăm hai mươi ba phẩy bốn mươi lăm"
    assert number_to_words(999.99) == "chín trăm chín mươi chín phẩy chín mươi chín"


def test_negative_numbers():
    """Test negative number conversion"""
    assert number_to_words(-5) == "âm năm"
    assert number_to_words(-10) == "âm mười"
    assert number_to_words(-21) == "âm hai mươi mốt"
    assert number_to_words(-123) == "âm một trăm hai mươi ba"
    assert number_to_words(-1000) == "âm một nghìn"

    # Negative decimals
    assert number_to_words(-1.5) == "âm một phẩy năm"
    assert number_to_words(-123.45) == "âm một trăm hai mươi ba phẩy bốn mươi lăm"


def test_large_numbers():
    """Test very large numbers"""
    # Thousands
    assert "nghìn" in number_to_words(1000)
    assert "nghìn" in number_to_words(123000)

    # Millions
    assert "triệu" in number_to_words(1000000)
    assert "triệu" in number_to_words(5000000)

    # Billions
    assert "tỷ" in number_to_words(1000000000)
    assert "tỷ" in number_to_words(1000000000000)

    # Very large number
    assert number_to_words(1000000000000) == "một nghìn tỷ"
    assert (
        number_to_words(1234567890)
        == "một tỷ hai trăm ba mươi bốn triệu năm trăm sáu mươi bảy nghìn tám trăm chín mươi"
    )


def test_edge_cases():
    """Test edge cases"""
    # Zero
    assert number_to_words(0) == "không"
    assert number_to_words(0.0) == "không"

    # Ten
    assert number_to_words(10) == "mười"

    # Hundred
    assert number_to_words(100) == "một trăm"

    # Thousand
    assert number_to_words(1000) == "một nghìn"

    # Numbers with zeros in middle
    assert number_to_words(101) == "một trăm linh một"
    assert number_to_words(1001) == "một nghìn không trăm linh một"
    assert number_to_words(1010) == "một nghìn không trăm mười"

    # Numbers ending in special digits
    assert number_to_words(15) == "mười lăm"
    assert number_to_words(25) == "hai mươi lăm"
    assert number_to_words(35) == "ba mươi lăm"
    assert number_to_words(21) == "hai mươi mốt"
    assert number_to_words(31) == "ba mươi mốt"


def test_string_input():
    """Test string number input"""
    assert number_to_words("123") == "một trăm hai mươi ba"
    assert number_to_words("1.5") == "một phẩy năm"
    assert number_to_words("-5") == "âm năm"


def test_invalid_input():
    """Test invalid input handling"""
    with pytest.raises(InvalidNumberError):
        number_to_words("abc")

    with pytest.raises(InvalidNumberError):
        number_to_words("12abc")

    with pytest.raises(InvalidNumberError):
        number_to_words(None)


def test_decimal_precision():
    """Test decimal numbers with different precision"""
    # Single decimal place
    assert number_to_words(1.1) == "một phẩy một"
    assert number_to_words(5.9) == "năm phẩy chín"

    # Multiple decimal places (natural representation)
    assert number_to_words(1.25) == "một phẩy hai mươi lăm"
    assert number_to_words(3.14) == "ba phẩy mười bốn"
    assert number_to_words(2.718) == "hai phẩy bảy trăm mười tám"


def test_zero_in_different_positions():
    """Test numbers with zeros in different positions"""
    assert number_to_words(10) == "mười"
    assert number_to_words(20) == "hai mươi"
    assert number_to_words(100) == "một trăm"
    assert number_to_words(200) == "hai trăm"
    assert number_to_words(1000) == "một nghìn"
    assert number_to_words(10000) == "mười nghìn"
    assert number_to_words(100000) == "một trăm nghìn"
    assert number_to_words(1000000) == "một triệu"


def test_consecutive_numbers():
    """Test consecutive small numbers"""
    assert number_to_words(1) == "một"
    assert number_to_words(2) == "hai"
    assert number_to_words(3) == "ba"
    assert number_to_words(4) == "bốn"
    assert number_to_words(5) == "năm"
    assert number_to_words(6) == "sáu"
    assert number_to_words(7) == "bảy"
    assert number_to_words(8) == "tám"
    assert number_to_words(9) == "chín"
