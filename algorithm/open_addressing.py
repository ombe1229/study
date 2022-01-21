"""
해시 테이블 - 개방 주소법
폐쇄 해싱
"""

from enum import Enum
from typing import Any
import hashlib


class Status(Enum):
    OCCUPIED = 0
    EMPTY = 1
    DELETED = 2


class Bucket:
    def __init__(
        self, key: Any = None, value: Any = None, stat: Status = Status.EMPTY
    ) -> None:
        self.key = key
        self.value = value
        self.stat = stat

    def set(self, key: Any, value: Any, stat: Status) -> None:
        self.key = key
        self.value = value
        self.stat = stat

    def set_status(self, stat: Status) -> None:
        self.stat = stat


class OpenHash:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.table = [Bucket()] * self.capacity

    def hash_value(self, key: Any) -> int:
        if isinstance(key, int):
            return key % self.capacity
        return int(hashlib.md5(str(key).encode()).hexdigest(), 16) % self.capacity

    def rehash_value(self, key: Any) -> int:
        return (self.hash_value(key) + 1) % self.capacity

    def search_node(self, key: Any) -> Any:
        hash = self.hash_value(key)
        buc = self.table[hash]

        for _ in range(self.capacity):
            if buc.stat == Status.EMPTY:
                break
            elif buc.stat == Status.OCCUPIED and buc.key == key:
                return buc
            hash = self.rehash_value(hash)
            buc = self.table[hash]
        return None

    def search(self, key: Any) -> Any:
        buc = self.search_node(key)
        if buc is not None:
            return buc.value
        else:
            return None

    def add(self, key: Any, value: Any) -> bool:
        if self.search(key) is not None:
            return False

        hash = self.hash_value(key)
        buc = self.table[hash]
        for i in range(self.capacity):
            if buc.stat == Status.EMPTY or buc.stat == Status.DELETED:
                self.table[hash] = Bucket(key, value, Status.OCCUPIED)
                return True
            hash = self.rehash_value(hash)
            buc = self.table[hash]
        return False

    def remove(self, key: Any) -> bool:
        buc = self.search_node(key)
        if buc is None:
            return False
        buc.set_status(Status.DELETED)
        return True

    def dump(self) -> None:
        for i in range(self.capacity):
            print(f"{i:2} ", end="")
            if self.table[i].stat == Status.OCCUPIED:
                print(f"{self.table[i].key} ({self.table[i].value})")
            elif self.table[i].stat == Status.EMPTY:
                print("Not registered")
            elif self.table[i].stat == Status.DELETED:
                print("Removed")
