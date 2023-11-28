class Stack:
    def __init__(self):
        self.MAX_SIZE = 3
        self.item = []
        self.top = -1

    def is_empty(self):
        return self.top < 0

    def push(self, element):
        if self.top >= self.MAX_SIZE - 1:
            print("Stack full on push")
        else:
            self.top += 1
            self.item.append(element)

    def pop(self):
        if self.is_empty():
            print("Stack empty on pop")
        else:
            self.top -= 1

    def get_top(self):
        if self.is_empty():
            print("Stack empty on getTop")
        else:
            stack_top = self.item[self.top]
            print(stack_top)

    def print_stack(self):
        print("[", end=" ")
        for i in range(self.top, -1, -1):
            print(self.item[i], end=" ")
        print("]")

if __name__ == "__main__":
    s = Stack()
    s.push(5)
    s.push(15)
    s.push(20)
    s.print_stack()
