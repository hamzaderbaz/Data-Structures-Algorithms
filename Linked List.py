class Node:
    def __init__(self, info):
        self.info = info
        self.next = None

class LinkedListType:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def list_size(self):
        return self.length

    def is_empty(self):
        return self.length == 0

    def insert_at(self, loc, item):
        if loc < 0 or loc > self.length:
            print("ERROR: Out of range")
        else:
            new_node = Node(item)
            if loc == 0:
                self.insert_first(item)
            elif loc == self.length:
                self.insert_end(item)
            else:
                current = self.first
                for i in range(1, loc):
                    current = current.next

                new_node.next = current.next
                current.next = new_node
                self.length += 1

    def insert_first(self, item):
        new_node = Node(item)
        if self.length == 0:
            self.first = self.last = new_node
            new_node.next = None
        else:
            new_node.next = self.first
            self.first = new_node
        self.length += 1

    def insert_end(self, item):
        new_node = Node(item)
        if self.length == 0:
            self.first = self.last = new_node
            new_node.next = None
        else:
            self.last.next = new_node
            new_node.next = None
            self.last = new_node
        self.length += 1

    def print_list(self):
        current = self.first
        while current:
            print(current.info)
            current = current.next


if __name__ == "__main__":
    l1 = LinkedListType()
    l1.insert_at(0, 10)
    l1.insert_at(1, 15)
    l1.insert_at(2, 20)
    l1.insert_at(3, 25)
    l1.print_list()
