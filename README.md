# vn-numberwords

Convert numbers to Vietnamese words (supports Northern and Southern variants).

## Install (from source)

```bash
pip install -e .
```

## Usage

```python
from vn_numberwords import number_to_words, number_to_currency, SouthDictionary

print(number_to_words(1234))                       # "một nghìn hai trăm linh bốn"
print(number_to_currency(1234, "đồng"))           # "một nghìn hai trăm linh bốn đồng"
print(number_to_words(21, SouthDictionary()))      # "hai mươi mốt"
```

Parse Vietnamese-formatted strings:

```python
from vn_numberwords import vietnamese_string_to_words

print(vietnamese_string_to_words("1.234.56"))     # decimal example
```

## CLI / Demo

Run the demo script:

```bash
python number2word.py
```

## License

MIT


