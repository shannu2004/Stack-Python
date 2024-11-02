class QueueNode:
    def __init__(self, val: int):
        self.val = val
        self.next = None

class MyQueue:
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, x: int) -> None:
        node = QueueNode(x)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def pop(self) -> int:
        temp = self.head
        self.head = temp.next
        return temp.val

    def peek(self) -> int:
        return self.head.val

    def empty(self) -> bool:
        return self.head is None


commands = ["MyQueue", "push", "push", "peek", "pop", "empty"]
args = [[], [1], [2], [], [], []]

output = []
queue = None

for command, arg in zip(commands, args):
    if command == "MyQueue":
        queue = MyQueue()
        output.append(None)
    elif command == "push":
        queue.push(arg[0])
        output.append(None)
    elif command == "peek":
        output.append(queue.peek())
    elif command == "pop":
        output.append(queue.pop())
    elif command == "empty":
        output.append(queue.empty())

print(output)
