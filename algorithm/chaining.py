"""
해시 테이블 - 체이닝
개방 해싱 + 폐쇄 해싱
"""

from typing import Any
import hashlib


class Node:
    def __init__(self, key: Any, value: Any, next: "Node") -> None:
        self.key = key
        self.value = value
        self.next = next


class ChainedHash:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.table = [None] * self.capacity

    def hash_value(self, key: Any) -> int:
        if isinstance(key, int):
            return key % self.capacity
        return int(hashlib.sha256(str(key).encode()).hexdigest(), 16) % self.capacity

    def search(self, key: Any) -> Any:
        hash = self.hash_value(key)
        node = self.table[hash]

        while node is not None:
            if node.key == key:
                return node.value
            node = node.next

        return None

    def add(self, key: Any, value: Any) -> bool:
        hash = self.hash_value(key)
        node = self.table[hash]

        while node is not None:
            if node.key == key:
                return False
            node = node.next

        temp = Node(key, value, self.table[hash])
        self.table[hash] = temp
        return True

    def remove(self, key: Any) -> bool:
        hash = self.hash_value(key)
        node = self.table[hash]
        prev = None

        while node is not None:
            if node.key == key:
                if prev is None:
                    self.table[hash] = node.next
                else:
                    prev.next = node.next
                return True
            prev = node
            node = node.next

        return False

    def dump(self) -> None:
        for i in range(self.capacity):
            node = self.table[i]
            print(i, end="")
            while node is not None:
                print(f" -> {node.key} ({node.value})", end="")
                node = node.next
            print()
