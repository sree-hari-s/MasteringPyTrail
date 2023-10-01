"""
Demonstrate good code formatting practices.

See https://peps.python.org/pep-0008/ for more information.
"""

import math
from random import randint
from typing import Union


GLOBAL_VARIABLE = 123


def random_number(max_value: int = 10) -> int:
    """Return a random number up to max_value."""
    return randint(0, max_value)


class Number:
    """Class to store information about a number."""

    def __init__(self: "Number", value: Union[int, float]) -> None:
        """Initialise instance."""
        self.value = value
        self._protected_attr = "protected"

    def __str__(self: "Number") -> str:
        """Return string representation of instance."""
        return str(self.value)

    def __add__(self: "Number", other: "Number") -> "Number":
        """Implement addition."""
        if not isinstance(other, Number):
            return NotImplemented
        return Number(self.value + other.value)

    def mul_by_pi(self: "Number") -> "Number":
        """Multiply by Pi and return instance."""
        self.value *= math.pi
        return self


if __name__ == "__main__":
    num1 = Number(2).mul_by_pi()
    num2 = Number(34)
    print(f"The result is: {num1 + num2}.")
