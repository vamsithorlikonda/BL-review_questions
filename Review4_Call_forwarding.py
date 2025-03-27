class CallQueue:
    def __init__(self):
        self.queue = []
        self.forwarding_number = None

    def enqueue(self, call):
        self.queue.append(call)
        print(f"Incoming Call is {call} added to queue")

    def dequeue(self):
        if self.is_empty():
            print("No calls in the queue")
            return None
        call = self.queue.pop(0)
        self.forward_call(call)
        return call

    def set_forwarding_number(self, number):
        self.forwarding_number = number
        print(f"Calls will be forwarded to: {number}")

    def forward_call(self, call):
        if self.forwarding_number is None:
            print(f"Call from {call} could not be forwarded")
        else:
            print(f"Call from {call} is forwarded to {self.forwarding_number}")

    def front(self):
        if self.is_empty():
            return None
        return self.queue[0]

    def rear(self):
        if self.is_empty():
            return None
        return self.queue[-1]

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

    def display(self):
        print("Call Queue:", self.queue)

cq = CallQueue()
cq.set_forwarding_number(input("Enter the number that you want to forwarded to:"))

cq.enqueue("9951710960")
cq.enqueue("9705220421")
cq.display()

cq.dequeue()
cq.display()

cq.dequeue()
cq.display()