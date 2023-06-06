class Queue:
    def __init__(self) -> None:
        self.queue = []

    def is_empty(self):
        return not self.queue

    def enqueue(self, value):
        self.queue.insert(0, value)

    def dequeue(self):
        if self.is_empty():
            raise ValueError("Queue underflow")
        value = self.queue.pop()
        return value

    def peek(self):
        if self.is_empty():
            raise ValueError("Queue underflow")
        value = self.queue[-1]
        return value

    def size(self):
        return len(self.queue)

    def __str__(self):
        """Returns a string representation of the queue"""
        str_repr = "FRONT -> " + ", ".join(reversed(self.queue)) + " <- REAR"
        return str_repr


if __name__ == '__main__':
    q = Queue()
    q.enqueue('order_1')
    q.enqueue('order_2')
    q.enqueue('order_3')
    q.enqueue('order_4')
    print(q)
    q.dequeue()
    print(q)
    q.dequeue()
    q.dequeue()
    print(q)
