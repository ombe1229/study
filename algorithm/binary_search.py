"""
이진 검색
"""

from typing import Any, Sequence
from random import randint


def binary_search(seq: Sequence, key: Any) -> int:
    first_index = 0
    last_index = len(seq) - 1
    while True:
        middle_index = (first_index + last_index) // 2
        if seq[middle_index] == key:
            return middle_index
        elif seq[middle_index] > key:
            last_index = middle_index + 1
        else:
            first_index = middle_index - 1
        if first_index > last_index:
            return -1
