heights = [132, 142, 170, 182, 155]
widths = [27.9, 32.0, 26.0, 14.1, 59.8, 48.8]

for h in heights:
    for w in widths:
        result = w * h
        # 文字列の先にfをつけるとf文字列(フォーマット文字列)になる
        # Pythonで小数を含む計算をする場合は、小数の桁数を指定して出力する
        # 文字列 ""
        # {}で囲むと変数が使える
        # . 小数点
        # 2 何桁まで
        # f 小数
        print(f"{result:.2f}")
