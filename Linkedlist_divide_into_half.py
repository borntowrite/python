
class Node:
    def __init__(self, val):
        self.value = val
        self.next = None
    def add(self, val):
        if self.next is None:
            self.next = Node(val)
        else:
            self.next.add(val)
    def printTree(self):
        print(self.value)
        if self.next:
            self.next.printTree()
    def divide(self):
        if self.value is None: return None
        runner = self
        fastrunner = self
        while fastrunner:
            print("fasterrunner: ", fastrunner.value)
            print("runner: ", runner.value)
            fastrunner = fastrunner.next
            if fastrunner is None: break
            fastrunner = fastrunner.next
            runner = runner.next
        runner.next = None
        return runner

c = Node(1)
c.add(2)
c.add(3)
c.add(4)
c.add(5)
c.add(6)
c.add(7)
c.add(8)
c.add(9)
c.add(10)
c.add(11)
#c.printTree()
c.divide()
