
class Stack:
    def __init__(self):
        self.top = -1
        self.size = 100
        self.arr = [0] * self.size

    def push(self, x: int) -> None:
        self.top += 1
        self.arr[self.top] = x

    def pop(self) -> int:
        x = self.arr[self.top]
        self.top -= 1
        return x

    def Top(self) -> int:
        return self.arr[self.top]

    def Size(self) -> int:
        return self.top + 1

if __name__ == "__main__":
    s = Stack()
    s.push(6)
    s.push(3)
    s.push(7)
    s.push(10)
    s.push(11)
    print("Top of stack is before deleting any element", s.Top())
    print("Size of stack before deleting any element", s.Size())
    print("The element deleted is", s.pop())
    print("Size of stack after deleting an element", s.Size())
    print("Top of stack after deleting an element", s.Top())


