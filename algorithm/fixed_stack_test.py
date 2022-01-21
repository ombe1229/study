from fixed_stack import FixedStack


stack = FixedStack(64)
stack.push("a")
stack.push("b")
print(f"({len(stack)} / {stack.capacity})")
stack.dump()
print(stack.pop())
stack.push("a")
stack.push("c")
stack.dump()
print(stack.peek())
print(stack.count("a"))
print(stack.find("d"))
print("c" in stack)
stack.clear()
stack.dump()
