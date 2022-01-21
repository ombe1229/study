from fixed_queue import FixedQueue


q = FixedQueue(64)
q.enque("a")
q.enque("b")
print(f"({len(q)} / {q.capacity})")
q.dump()
print(q.deque())
q.enque("c")
print(q.peek())
q.dump()
q.enque("b")
print(q.find("b"))
