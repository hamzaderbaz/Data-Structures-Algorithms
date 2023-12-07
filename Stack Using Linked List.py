class Stack:
    class StackNode:
        def __init__(self, item):
            self.item = item
            self.next = None

    def __init__(self):
        self.topPtr = None

    def is_empty(self):
        return self.topPtr is None

    def push(self, new_item):
        new_node = self.StackNode(new_item)
        new_node.next = self.topPtr
        self.topPtr = new_node

    def pop(self):
        if self.is_empty():
            print("Stack empty on pop")
        else:
            temp = self.topPtr
            self.topPtr = self.topPtr.next
            temp.next = None
            del temp

    def get_top(self):
        if self.is_empty():
            print("Stack empty on getTop")
        else:
            stack_top = self.topPtr.item
            print("\nTop Element of the stack is", stack_top)
            print()

    def display(self):
        cur_ptr = self.topPtr
        print("\nItems in the stack : ", end="")
        print("[ ", end="")
        while cur_ptr is not None:
            print(cur_ptr.item, end=" ")
            cur_ptr = cur_ptr.next
        print("]")

if __name__ == "__main__":
    s = Stack()
    s.push(10)
    s.display()
