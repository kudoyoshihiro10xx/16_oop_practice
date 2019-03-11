import math


class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

    def diagonal(self):
        """対角線の長さ"""
        return math.sqrt(self.side ** 2 + self.side ** 2)


def main():
    # 1辺の長さが 1 の正方形
    square1 = Square(side=1)

    print(square1.area())
    print(square1.diagonal())

    # 1辺の長さが 4 の正方形
    square2 = Square(side=4)

    print(square2.area())
    print(square2.diagonal())


if __name__ == '__main__':
    main()
