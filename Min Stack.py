class MinStack:
    def __init__(self):
        self.mainStack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.mainStack.append(val)
        if not self.minStack or val <= self.minStack[-1]:
            self.minStack.append(val)

    def pop(self) -> None:
        popped = self.mainStack.pop()
        if popped == self.minStack[-1]:
            self.minStack.pop()

    def top(self) -> int:
        return self.mainStack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]



min_stack = MinStack()


operations = ["MinStack", "push", "push", "push", "getMin", "pop", "top", "getMin"]
arguments = [[], [-2], [0], [-3], [], [], [], []]

# To store results
results = []

for op, arg in zip(operations, arguments):
    if op == "MinStack":
        results.append(None)  
    elif op == "push":
        min_stack.push(arg[0])
        results.append(None)  
    elif op == "pop":
        min_stack.pop()
        results.append(None)  
    elif op == "top":
        results.append(min_stack.top())  
    elif op == "getMin":
        results.append(min_stack.getMin())  


print(results)  
