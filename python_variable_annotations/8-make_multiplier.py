#!/usr/bin/env python3
"""type-annotated function make_multiplier that takes a
float multiplier as argument"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """returns a function that multiplies a float
    by multiplier."""
    def multiplicar(n: float) -> float:
        """Multiplicará el multiplier por n"""
        return n * multiplier
    return multiplicar
