class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = float('inf')

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.min = x if self.min > x else self.min
        self.stack.append(self.min)
        self.stack.append(x)

    def pop(self):
        """
        :rtype: void
        """
        self.stack.pop()
        self.stack.pop()
        self.min = float('inf') if len(self.stack) == 0 else self.stack[-2]

    def top(self):
        """
        :rtype: int
        """
        return None if len(self.stack) < 2 else self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return None if len(self.stack) < 2 else self.stack[-2]

# Your MinStack object will be instantiated and called as such:
obj = MinStack()
print(obj.push(-2))
print(obj.push(0))
print(obj.push(-3))
print(obj.getMin())
print(obj.pop())
print(obj.top())
print(obj.getMin())
