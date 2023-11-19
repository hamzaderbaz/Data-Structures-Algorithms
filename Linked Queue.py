class Node:
    def __init__(self, item):
        self.item = item
        self.next = None

class LinkedQueue:
    def __init__(self):
        self.length = 0
        self.front_ptr = None
        self.rear_ptr = None

    def is_empty(self):
        return self.length == 0

    def dequeue(self):
        if self.is_empty():
            print("Empty Queue")
        elif self.length == 1:
            del self.front_ptr
            self.rear_ptr = None
            self.length = 0
        else:
            current = self.front_ptr
            self.front_ptr = self.front_ptr.next
            del current
            self.length -= 1

    def enqueue(self, item):
        new_node = Node(item)
        new_node.next = None

        if self.length == 0:
            self.rear_ptr = self.front_ptr = new_node
        else:
            self.rear_ptr.next = new_node
            self.rear_ptr = new_node
        self.length += 1

    def front(self):
        assert not self.is_empty()
        return self.front_ptr.item

    def rear(self):
        assert not self.is_empty()
        return self.rear_ptr.item

    def clear_queue(self):
        current = self.front_ptr

        while current is not None:
            temp = current
            current = current.next
            del temp

        self.rear_ptr = None
        self.length = 0

    def display(self):
        current = self.front_ptr
        print("Item in the queue: [ ", end="")
        while current is not None:
            print(current.item, end=" ")
            current = current.next
        print("]")

    def search(self, item):
        current = self.front_ptr
        flag = True
        while current is not None:
            if current.item == item:
                print(f"The item: {item} found")
                flag = False
                break
            current = current.next
        if flag:
            print(f"The item: {item} not found")


if __name__ == "__main__":
    q1 = LinkedQueue()

    for i in range(1, 21):
        q1.enqueue(i)

    print(q1.front())
    print(q1.rear())
    q1.display()
