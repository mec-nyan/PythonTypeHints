#!/usr/bin/env python3 
'''How to use type annotations in Python.'''


from typing import Union, Optional


# Use python annotations in variables (built-in types)
name: str = 'Paul'
surname: str = 'Gilbert'
age: int = 40
speed: float = 180.4
active: bool = True

guitars: list[str] = ['Gibson', 'Epiphone', 'Jackson', 'Ibanez']

# How to annotate a function definition
def say_hi(name: str) -> str:
    return f'Hi, { name }!'

# Call the function
# This will be OK
say_hi(name)

# This will throw an error
say_hi(age)

# Type aliases
Vector = list[float]

temps: Vector = [32.1, 23.5, 29.01, 23.5]

# Unions
def set_price(base: Union[int, float]) -> float:
    return base * 1.5

set_price(100)      # OK
set_price(10.5)     # Also OK

# Optional
def how_much(base: Union[int, float], percentage: int, prefix: Optional[str] = None) -> str:
    total: float = (base / 100) * percentage
    return 'The price is "{}{}"'.format(prefix and f'{ prefix } ' or '', total)


print(how_much(100, 20))
print(how_much(200, 32, 'USD'))


