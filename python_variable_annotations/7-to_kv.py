#!/usr/bin/env python3
"""type-annotated function to_kv that takes a string k and
an int OR float v as arguments and returns a tuple."""
from typing import List, Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """return a tupla, The first element of the tuple is the string k.
    The second element is the square of the int/float v
    and should be annotated as a float."""
    return (k, v**2)
