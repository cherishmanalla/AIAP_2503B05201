def add(a, b):
    return a + b


def count_down(n):
    while n >= 0:
        print(n)
        n -= 1


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width


numbers = [1, 2, 3]
index = 5
if 0 <= index < len(numbers):
    print(numbers[index])
else:
    print("Index out of range")
