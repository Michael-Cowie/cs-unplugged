```python
original = input('Please enter a number between 0 and 31: ')
number = int(original)
bit_value = 32
cards = ''
while bit_value > 1:
  bit_value = bit_value / 2
  if number >= bit_value:
    cards = cards + 'W'
    number = number - bit_value
  else:
    cards = cards + 'B'
print('The binary representation for the number ' + str(original) + ' is ' + str(cards))
```