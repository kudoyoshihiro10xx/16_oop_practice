class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def profile(self):
        return f"Name: {self.name}, Age: {self.age}"


if __name__ == '__main__':
    # 'クラス'を使うイメージ
    bob = Person("Bob", 15)  # インスタンス化
    print(bob.profile())  # 'Name: Bob, Age: 15'と出力されて欲しい

    tom = Person("Tom", 24)  #インスタンス化
    print(tom.profile())  # 'Name: Tom, age: 24'と出力されて欲しい

    ken = Person("Ken", 42)  #インスタンス化
    print(ken.profile())
