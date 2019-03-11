class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        # 円の面積 = 半径 * 半径 * 円周率
        return (self.radius ** 2) * 3.14

    def circumference(self):
        return 2 * self.radius * 3.14


if __name__ == '__main__':
    # 半径が 1 の円
    circle1 = Circle(radius=3)  # インスタンス化

    # circle1の面積を求める
    print(circle1.area())

    # circle2の面積を求める
    circle2 = Circle(20)
    print(circle2.area())

    # ユーザーから、半径の長さを入力して受け取り、その面積を出力する

    data = int(input("半径を入力して下さい: "))
    circle3 = Circle(data)
    print(circle3.area())

    # 円周を求める
    print(circle3.circumference())
    print(circle1.radius)
