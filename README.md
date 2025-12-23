# vn-numberwords

[![PyPI version](https://badge.fury.io/py/vn-numberwords.svg)](https://badge.fury.io/py/vn-numberwords)
[![Python versions](https://img.shields.io/pypi/pyversions/vn-numberwords.svg)](https://pypi.org/project/vn-numberwords/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![CI](https://github.com/rato-kaz/vn-numberwords/actions/workflows/ci.yml/badge.svg)](https://github.com/rato-kaz/vn-numberwords/actions/workflows/ci.yml)

Convert numbers to Vietnamese words and Vietnamese words to numbers (supports Northern and Southern variants).

## Installation

```bash
pip install vn-numberwords
```

## Usage

```python
from vn_numberwords import number_to_words, number_to_currency, words_to_number, currency_words_to_number, SouthDictionary

# Convert numbers to Vietnamese words
print(number_to_words(1234))                       # "một nghìn hai trăm linh bốn"
print(number_to_currency(1234, "đồng"))           # "một nghìn hai trăm linh bốn đồng"
print(number_to_words(21, SouthDictionary()))      # "hai mươi mốt"

# Convert Vietnamese words to numbers
print(words_to_number("một nghìn hai trăm linh bốn"))  # 1234
print(words_to_number("mười một"))                     # 11
print(words_to_number("một trăm ngàn tỷ"))             # 100000000000000
print(currency_words_to_number("một nghìn đồng"))      # 1000
```

Parse Vietnamese-formatted strings:

```python
from vn_numberwords import vietnamese_string_to_words

print(vietnamese_string_to_words("1.234.56"))     # decimal example
```

## Features

### Number to Words
- Convert numbers to Vietnamese words
- Support for Northern and Southern Vietnamese variants
- Currency formatting
- Large number support (up to trillions)

### Words to Number
- Convert Vietnamese words back to numbers
- Support for both accented and non-accented Vietnamese
- Handle complex numbers with multiple magnitude keywords
- Currency parsing

### Supported Number Formats
- Units: không, một, hai, ba, bốn, năm, sáu, bảy, tám, chín
- Tens: mười, mươi, chục
- Hundreds: trăm
- Thousands: nghìn, ngàn, nghàn
- Millions: triệu
- Billions: tỷ, tỉ

## CLI / Demo

Run the demo script:

```bash
python number2word.py
```

## License

MIT


