class ArrayListType:
    def __init__(self, size=100):
        if size <= 0:
            print("Wrong Size")
            self.maxSize = 100
        else:
            self.maxSize = size

        self.length = 0
        self.list = [0] * self.maxSize

    def isEmpty(self):
        return self.length == 0

    def isFull(self):
        return self.length == self.maxSize

    def listSize(self):
        return self.length

    def maxListSize(self):
        return self.maxSize

    def print(self):
        for i in range(self.length):
            print(self.list[i], end=" ")
        print()

    def isItemAtEqual(self, loc, item):
        if loc < 0 or loc >= self.length:
            return False
        else:
            return self.list[loc] == item

    def insertAt(self, loc, item):
        if self.isFull():
            print("The List is Full")
        elif loc < 0 or loc > self.length:
            print("Out of Range")
        else:
            self.list.insert(loc, item)
            self.length += 1

    def insertEnd(self, item):
        if self.isFull():
            print("The List is Full")
        else:
            self.list[self.length] = item
            self.length += 1

    def retrieveAt(self, loc):
        if loc < 0 or loc >= self.length:
            print("Out of Range")
        else:
            return self.list[loc]

    def replaceAt(self, loc, item):
        if loc < 0 or loc >= self.length:
            print("Out of Range")
        else:
            self.list[loc] = item

    def clearList(self):
        self.length = 0

    def seqSearch(self, item):
        for loc in range(self.length):
            if self.list[loc] == item:
                return loc
        return -1

    def insertNoDuplicate(self, item):
        if self.isFull():
            print("The List is Full")
        else:
            flag = self.seqSearch(item)
            if flag == -1:
                self.list[self.length] = item
                self.length += 1
            else:
                print("No duplicates are allowed.")

    def remove(self, item):
        loc = self.seqSearch(item)
        if loc == -1:
            print("The item to be deleted is not in the list")
        else:
            self.removeAt(loc)

    def removeAt(self, loc):
        if loc < 0 or loc >= self.length:
            print("The location of the item to be removed is out of range.")
        else:
            self.list.pop(loc)
            self.length -= 1

# Test the class
if __name__ == "__main__":
    lst1 = ArrayListType()
    for i in range(20):
        lst1.insertAt(i, i * i)

    lst1.print()

    x = lst1.retrieveAt(10)
    print(x)

    lst2 = ArrayListType(lst1)

    lst2.print()
