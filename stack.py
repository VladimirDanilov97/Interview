class Stack():
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        if self.stack:
            return False
        return True
    
    def push(self, item):
        self.stack.insert(0, item)

    def pop(self):
        return self.stack.pop(0)

    def peek(self):
        return self.stack[0]

    def size(self):
        return len(self.stack)
    
    def __str__(self):
        return f'{self.stack}'

if __name__ == '__main__':
    s = Stack()
    print(s.isEmpty())
    s.push(1)
    s.push(3)
    s.push(6)
    print(s)
    s.pop()
    print(s)
    print(s.isEmpty())
    
