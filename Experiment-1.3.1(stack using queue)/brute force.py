from collections import deque
class MyStack:

    def __init__(self):
        self.q = deque()

    def push(self, x):
        self.q.append(x)

        # Rotate the queue
        for i in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self):
        return self.q.popleft()

    def top(self):
        return self.q[0]

    def empty(self):
        return len(self.q) == 0

stack = MyStack()

stack.push(1)
stack.push(12)
stack.push(5)

print("Top:", stack.top())      
print("Pop:", stack.pop())      
print("Top:", stack.top())  
print("Empty:", stack.empty())  

stack.pop()
stack.pop()

print("Empty:", stack.empty())  