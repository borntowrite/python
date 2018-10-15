#######################################
# Queue
########################################
import collections

class queue:
    
    def __init__(self):
        self.queue = list()
        
    def addtoright(self, val):
        if val not in self.queue:
            self.queue.insert(0, val)
            return True
        return False
            
    def removefromleft(self):
        if len(self.queue)>0:
            return self.queue.pop()

    def leftpeek(self):
        if len(self.queue)>0:
            return self.queue[0]

    def rightpeek(self):
        if len(self.queue)>0:
            return self.queue[-1]
            
    def print(self):
        print(self.queue)

q = queue()
q.addtoright(1)
q.addtoright(2)
q.addtoright(3)
q.addtoright(4)
q.addtoright(5)
q.print()
q.removefromleft()
q.print()
print(q.leftpeek())
print(q.rightpeek())

