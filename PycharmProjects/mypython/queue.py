class Queue:

        def __init__(self):
            self.size: int = 0
            self.queue: list = []

        def is_empty(self):
            if self.size == 0:
                return self.size


        def append(self, item):
            self.queue.append(item)
            self.size += 1

        def get_size(self):
            return self.size

        def popleft(self):
            self.queue.remove(self.queue[0])
            self.size -= 1

        def dequeue(self):
            return self.queue.pop(0)

