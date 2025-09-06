s = {1, 2, 3}
print("Initial Set:", s)


s.add(4)
print("After add(4):", s)


s.remove(2)
print("After remove(2):", s)


s.discard(5)
print("After discard(5):", s)


popped_element = s.pop()
print("Popped Element:", popped_element)
print("After pop():", s)


s.clear()
print("After clear():", s)
