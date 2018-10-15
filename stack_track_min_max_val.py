############################################
# Stack - track max value 
############################################
class stackmax:
    def __init__(self):
        self.stack = []
        self.max = []
    def add(self, val):
        self.stack.append(val)
        if len(self.max) !=0:
            if self.maxval() < val:
                self.max.append(val)
        else:
            self.max.append(val)
    def remove(self):
        if len(self.stack) != 0:
            x = self.stack.pop()
        if x == self.max[-1]:
            self.max.pop()
    def maxval(self):
        return self.max[-1]
    def printstack(self):
        print("stack: ",self.stack)
    def printmax(self):
        print("max: ", self.max)

m = stackmax()
m.add(3)
m.add(5)
m.add(1)
m.add(7)
m.printstack()
print('max val in stack', m.maxval())
# m.printmax()


############################################
# Stack - track min value 
############################################
class stackmin:
    def __init__(self):
        self.stack = []
        self.min = []
    def add(self, val):
        self.stack.append(val)
        if len(self.min) !=0:
            if self.minval() > val:
                self.min.append(val)
        else:
            self.min.append(val)
    def remove(self):
        x = self.stack.pop()
        if x == self.min[-1]:
            self.min.pop()
    def minval(self):
        return self.min[-1]
    def printstack(self):
        print("stack: ",self.stack)
    def printmin(self):
        print("min: ", self.min)

s = stackmin()
s.add(3)
s.add(5)
s.add(1)
s.add(7)
s.printstack()
# print(s.minval())
s.printmin()
s.remove()
s.printstack()
s.printmin()
s.remove()
s.printstack()
s.printmin() 