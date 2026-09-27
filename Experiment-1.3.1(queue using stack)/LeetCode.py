class MyQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x):
        self.s1.append(x)

    def pop(self):
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2.pop()

    def peek(self):
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2[-1]

    def empty(self):
        return len(self.s1) == 0 and len(self.s2) == 0
        
q = MyQueue()

q.push(1)
q.push(2)
q.push(3)

print("Front:", q.peek())     
print("Pop:", q.pop())        
print("Front:", q.peek())     
print("Empty:", q.empty())    

q.pop()
q.pop()

print("Empty:", q.empty())   