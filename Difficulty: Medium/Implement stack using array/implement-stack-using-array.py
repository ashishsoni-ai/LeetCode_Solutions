class myStack:
    def __init__(self, n):
        # Define Data Structures
        self.n = n
        self.st = []

    
    def isEmpty(self):
        # Check if stack is empty
        if len(self.st) == 0:
            return True
        return False

    
    def isFull(self):
        # Check if stack is full
        if len(self.st) == self.n:
            return True
        return False

    
    def push(self, x):
        # Insert x at the top of the stack
        if len(self.st) == self.n:
            return -1
        self.st.append(x)

    
    def pop(self):
        # Removes an element from the top of the stack
        if self.isEmpty():
            return -1
        self.st.pop()

    
    def peek(self):
        # Returns the top element of the stack
        if self.isEmpty():
            return -1
        return self.st[-1]
        