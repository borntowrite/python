
############################################
# General Stack
############################################
class Stack:
    def __init__(self):
        self.stack = []
    def add(self, val):
        if val not in self.stack:
            self.stack.append(val)
            return True
        else:
            return False
    def remove(self):
        if len(self.stack) > 0:
            self.stack.pop()
        else:
            print("no more elements")
    def peek(self):
        return self.stack[-1]
    def print_(self):
        print(self.stack)

d = Stack()
d.add(3) # add to right always
d.add(4)
d.add(5)
d.add(6)
d.print_()
print(d.peek()) # peek is always right one
d.add(12321)
d.add(1)
d.print_()
d.remove() # remove from right
d.print_()
print(d.peek())

