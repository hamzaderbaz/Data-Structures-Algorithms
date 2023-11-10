class DoublyLinkedList:
    class Node:
        def __init__(self, item):
            self.item = item
            self.next = None
            self.prev = None

    def __init__(self):
        self.first = None
        self.last = None
        self.count = 0

    def is_empty(self):
        return self.first is None

    def destroy(self):
        while self.first is not None:
            temp = self.first
            self.first = self.first.next
            del temp
        self.last = None
        self.count = 0

    def insert_last(self, val):
        new_node = self.Node(val)
        if self.count == 0:
            self.first = self.last = new_node
            new_node.next = new_node.prev = None
        else:
            new_node.next = None
            new_node.prev = self.last
            self.last.next = new_node
            self.last = new_node
        self.count += 1

    def insert_first(self, item):
        new_node = self.Node(item)
        if self.count == 0:
            self.first = self.last = new_node
            new_node.next = new_node.prev = None
        else:
            new_node.next = self.first
            new_node.prev = None
            self.first.prev = new_node
            self.first = new_node
        self.count += 1

    def insert_at(self, pos, item):
        if pos < 0 or pos > self.count:
            print("Out Of Range ...!")
        else:
            new_node = self.Node(item)
            if pos == 0:
                self.insert_first(item)
            elif pos == self.count:
                self.insert_last(item)
            else:
                current = self.first
                for i in range(1, pos):
                    current = current.next
                new_node.next = current.next
                new_node.prev = current
                current.next.prev = new_node
                current.next = new_node
                self.count += 1

    def remove_first(self):
        if self.count == 0:
            print("Empty List")
        elif self.count == 1:
            del self.first
            self.last = self.first = None
        else:
            current = self.first
            self.first = self.first.next
            self.first.prev = None
            del current
        self.count -= 1

    def delete_nth_node(self, pos):
        if pos < 0 or pos >= self.count:
            print("Out Of Range")
            return
        elif pos == 0:
            self.remove_first()
        elif pos == self.count - 1:
            self.remove_last()
        else:
            current = self.first.next
            for i in range(1, pos):
                current = current.next
            current.prev.next = current.next
            current.next.prev = current.prev
            del current
        self.count -= 1

    def remove_last(self):
        if self.count == 0:
            print("Empty List")
        elif self.count == 1:
            del self.first
            self.last = self.first = None
        else:
            current = self.last
            self.last = self.last.prev
            self.last.next = None
            del current
        self.count -= 1

    def remove(self, item):
        if self.is_empty():
            print("Empty List Can't Remove ")
            return
        current = self.first.next

        if self.first.item == item:
            self.remove_first()
            return
        else:
            while current is not None:
                if current.item == item:
                    break
                current = current.next

            if current is None:
                print("The item is not there")
                return
            elif current.next is None:
                self.remove_last()
                return
            else:
                current.prev.next = current.next
                current.next.prev = current.prev
                del current
                self.count -= 1

    def display(self):
        if self.is_empty():
            print("Empty List Can't Display...!")
        else:
            temp = self.first
            while temp is not None:
                print(temp.item, end=" ")
                temp = temp.next
        print()

    def reverse_display(self):
        if self.is_empty():
            print("Empty List Can't Display Reverse...!")
        else:
            temp = self.last
            while temp is not None:
                print(temp.item, end=" ")
                temp = temp.prev
        print()


if __name__ == "__main__":
    dl = DoublyLinkedList()
    dl.insert_at(0, 4)
    dl.insert_at(1, 6)
    dl.insert_at(2, 7)
    dl.insert_first(2)
    dl.insert_last(10)
    dl.remove(7)
    dl.display()
    dl.reverse_display()
