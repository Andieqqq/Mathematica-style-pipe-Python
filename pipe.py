from __future__ import annotations

from doctest import testmod
from operator import add, mul, sub
from typing import Any, Callable

__all__ = ["pipe"]
__author__ = "wuyudi"
__license__ = "MIT"
__version__ = "1.0.0"


class pipe:
    """A pipe
    >>> pipe(5) // (lambda x: add(x, 2)) // (lambda x: mul(x, 2)) // (lambda x: sub(x, 5))
    9

    In Mathematica, we write
    5 // Plus[#, 2] & // Times[#, 2] & //  Subtract[#, 5] &
    """

    def __init__(self: pipe, x: Any):
        self.x: Any = x

    def __floordiv__(self: pipe, func: Callable[[Any], Any]) -> pipe:
        return pipe(func(self.x))

    def __repr__(self: pipe) -> str:
        return str(self.x)


if __name__ == "__main__":
    testmod()
    (
        pipe(5)
        // (lambda x: add(2, x))
        // (lambda x: mul(2, x))
        // (lambda x: sub(x, 5))
        // print
    )
