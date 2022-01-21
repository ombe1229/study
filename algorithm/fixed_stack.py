from typing import Any


class FixedStack:
    class Empty(Exception):
        pass

    class Full(Exception):
        pass

    def __init__(self, capacity: int = 256) -> None:
        self.stk = [None] * capacity
        self.capacity = capacity
        self.ptr = 0

    def __len__(self) -> int:
        return self.ptr

    def is_empty(self) -> bool:
        return self.ptr <= 0

    def is_full(self) -> bool:
        return self.ptr >= self.capacity

    def push(self, value: Any) -> None:
        if self.is_full():
            raise FixedStack.Full
        self.stk[self.ptr] = value
        self.ptr += 1

    def pop(self) -> Any:
        if self.is_empty():
            raise FixedStack.Empty
        self.ptr -= 1
        return self.stk[self.ptr]

    def peek(self) -> Any:
        if self.is_empty():
            raise FixedStack.Empty
        return self.stk[self.ptr - 1]

    def clear(self) -> None:
        self.ptr = 0

    def find(self, value: Any) -> Any:
        for i in range(self.ptr - 1, -1, -1):
            if self.stk[i] == value:
                return i
        return -1

    def count(self, value: Any) -> int:
        count = 0
        for i in range(self.ptr):
            if self.stk[i] == value:
                count += 1
        return count

    def __contains__(self, value: Any) -> bool:
        """
        __contains__() 함수를 정의할 경우 인스턴스에 in 연산자 적용 가능
        """
        return self.count(value) > 0

    def dump(self) -> None:
        if self.is_empty():
            print("Stack is empty")
        else:
            print(self.stk[: self.ptr])
