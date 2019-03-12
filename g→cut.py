class Change:
    def __init__(self, carat, gram, lb):
        self.carat = carat
        self.gram = gram
        self.lb = lb

    def carat_gram(self):
        return self.carat * 0.2  # カラットからグラム

    # def carat_bl(self):
    #     return self.carat * 0.00044 #カラットからポンド
    #
    # def gram_carat(self):
    #     return self.gram * 5  #グラムからカラット
    #
    # def gram_lb(self):
    #     return self.gram * 0.0022046 #グラムからポンド
    #
    # def lb_carat(self):
    #     return self.lb * 2267.96  #ポンドからカラット
    #
    # def lb_gram(self):
    #     return self.lb * 453.592   #ポンドからグラム


if __name__ == '__main__':

    eee = print("入力したい単位は次の内どれですか？: [carat, gram, lb]")
    fff = print("変換したい単位は次の内どれですか？: [carat, gram, lb]")
    ggg = print("その値は？:")

    if eee == "carat":
        if fff == "gram":
            aaa = Change(ggg, 0, 0)
            iii = aaa.carat_gram()
            print(iii)
        else:
            aaa = Change(ggg, 0, 0)
            iii = aaa.carat_bl()
            print(iii)
    elif eee == "gram":
        if fff == "carat":
            aaa = Change(0, ggg, 0)
            iii = aaa.gram_carat()
            print(iii)
        else:
            aaa = Change(0, ggg, 0)
            iii = aaa.gram_lb()
            print(iii)
    else:
        if fff == "carat":
            aaa = Change(0, 0, ggg)
            iii = aaa.lb_carat()
            print(iii)
        else:
            aaa = Change(0, 0, ggg)
            iii = aaa.lb_gram()
            print(iii)
