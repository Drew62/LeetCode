# Design a stack class that supports the push, pop, top, and getMin operations.
#
#     MinStack() initializes the stack object.
#     void push(int val) pushes the element val onto the stack.
#     void pop() removes the element on the top of the stack.
#     int top() gets the top element of the stack.
#     int getMin() retrieves the minimum element in the stack.
#
# Each function should run in O(1)O(1) time.

class MinStack:

    def __init__(self):
        self.stack = [] 
        self.min = []

    def push(self, val: int) -> None:
        if isinstance(val, int):
            self.stack.append(val)
            
            if self.min == []:
                self.min.append(val)
            else:
                if val < self.min[-1]:
                    self.min.append(val)
                else:
                    self.min.append(self.min[-1])
            
    def pop(self) -> None:
        self.stack.pop()
        self.min.pop()

    def top(self) -> int:
       return self.stack[-1]

    def getMin(self) -> int:
        return self.min[-1]

stack = MinStack()
stack.push(3)
stack.push(2)
stack.push(4)
print(f"{stack.getMin()}")
stack.push(1)
print(f"{stack.getMin()}")

