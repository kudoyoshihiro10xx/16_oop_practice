class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


if __name__ == '__main__':
    # 横: 4 縦: 3 の長方形
    r1 = Rectangle(4, 3)  # インスタンス化

    # 3分課題:
    area1 = r1.area()  # 面積を計算する
    print(area1)  # 12が出力される
