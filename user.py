class User:
    def __init__(self, first_name, family_name):
        self.first_name = first_name
        self.family_name = family_name

    def full_name(self):
        return f"{self.family_name} {self.first_name}"


if __name__ == '__main__':
    masashi = User("まさし", "つちや")

    print(masashi.full_name())  # 'つちや まさし' って出力されてほしい
