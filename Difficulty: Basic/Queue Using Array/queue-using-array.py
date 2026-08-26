class myQueue:
    def __init__(self, n):
        self.arr = [0] * n
        self.front = 0
        self.rear = 0
        self.size = 0
        self.capacity = n
    
    def isEmpty(self):
        return self.size == 0
    
    def isFull(self):
        return self.size == self.capacity
    
    def enqueue(self, x):
        if self.isFull():
            return False
    
        self.arr[self.rear] = x
        self.rear = (self.rear + 1) % self.capacity
        self.size += 1
        return True
    
    def dequeue(self):
        if self.isEmpty():
            return -1
    
        x = self.arr[self.front]
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return x
    
    def getFront(self):
        if self.isEmpty():
            return -1
    
        return self.arr[self.front]
    
    def getRear(self):
        if self.isEmpty():
            return -1
    
        return self.arr[(self.rear - 1 + self.capacity) % self.capacity]