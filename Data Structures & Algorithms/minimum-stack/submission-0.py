import math
class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []
    
    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minstack:
            self.minstack.append(val)
        elif self.minstack[-1] >= val:
            self.minstack.append(val)

    def pop(self) -> None:
        #need to also delete it from self.minstack
        if self.stack[-1] == self.minstack[-1]:
            del self.minstack[-1]
        del self.stack[-1]

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minstack[-1]
