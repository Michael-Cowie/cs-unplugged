```python
original = input('Please enter a decimal number: ')
number = int(original)
bit_value = 1
cards = ''
while number >= bit_value:
  bit_value = bit_value * 2
while bit_value > 1:
  bit_value = bit_value / 2
  if number >= bit_value:
    cards = cards + 'W'
    number = number - bit_value
  else:
    cards = cards + 'B'
print('The binary representation for the number ' + str(original) + ' is ' + str(cards))
```