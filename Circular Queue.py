class ArrayQueueType:
    def __init__(self, size):
        if size <= 0:
            self.maxSize = 100
        else:
            self.maxSize = size

        self.front = 0
        self.arr = [0] * self.maxSize
        self.rear = self.maxSize - 1
        self.length = 0

    def is_empty(self):
        return self.length == 0

    def is_full(self):
        return self.length == self.maxSize

    def add_queue(self, element):
        if self.is_full():
            print("Queue Full Can't Enqueue ...!")
        else:
            self.rear = (self.rear + 1) % self.maxSize
            self.arr[self.rear] = element
            self.length += 1

    def delete_queue(self):
        if self.is_empty():
            print("Empty Queue Can't Dequeue ...!")
        else:
            self.front = (self.front + 1) % self.maxSize
            self.length -= 1

    def front_queue(self):
        assert not self.is_empty()
        return self.arr[self.front]

    def rear_queue(self):
        assert not self.is_empty()
        return self.arr[self.rear]

    def print_queue(self):
        if not self.is_empty():
            i = self.front
            while i != self.rear:
                print(self.arr[i], end=" ")
                i = (i + 1) % self.maxSize
            print(self.arr[self.rear])
        else:
            print("Empty Queue")

    def queue_search(self, element):
        pos = -1
        if not self.is_empty():
            i = self.front
            while i != self.rear:
                if self.arr[i] == element:
                    pos = i
                    break
                i = (i + 1) % self.maxSize
            if pos == -1:
                if self.arr[self.rear] == element:
                    pos = self.rear
        else:
            print("Queue is empty!")
        return pos

    def __del__(self):
        del self.arr

if __name__ == "__main__":
    q1 = ArrayQueueType(5)
    q1.add_queue(10)
    q1.add_queue(20)
    q1.add_queue(30)
    q1.add_queue(40)
    q1.add_queue(50)
    q1.print_queue()
