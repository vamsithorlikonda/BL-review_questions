class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, key):
        self.queue.append(key)
        print(f"Enqueued element is: {key}")

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        return self.queue.pop(0)
    
    def front(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        return self.queue[0]
    
    def rear(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        return self.queue[-1]
    
    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

    def display(self):
        print("Queue:", self.queue)

q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.display()

q.display()
print("First element is",q.front())
print("last element is ",q.rear())
print("Queue Size:", q.size())
