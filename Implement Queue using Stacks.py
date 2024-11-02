class MyQueue:

    def __init__(self):
        self.stack = []
        
    def push(self, x: int) -> None:
        self.stack.append(x)
        
    def pop(self) -> int:
        if self.empty():
            raise IndexError("pop from an empty queue")
        return self.stack.pop(0)
        
    def peek(self) -> int:
        if self.empty():
            raise IndexError("peek from an empty queue")
        return self.stack[0]
        
    def empty(self) -> bool:
        return len(self.stack) == 0



if __name__ == "__main__":
    queue = MyQueue()
    print(queue.push(1))  
    print(queue.push(2))  
    print(queue.peek())    
    print(queue.pop())     
    print(queue.empty())   
