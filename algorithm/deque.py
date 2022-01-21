from collections import deque


deq = deque(["a", "b", "c"])
deq.appendleft(0)
print(deq)
c = deq.copy()  # shallow copy
deq.extend([1, 2, 3, 4, 5])
deq.extendleft([1, 2, 3, 4, 5])
print(deq)
print(deq.index(1, 3, 7))
deq.reverse()
print(deq)
deq.rotate(3)
print(deq)
