# Nは1~50で、N=50の時、出力は555555である
# よって、1~555555を一つずつ調べる方法を用いる
N = int(input())
x = 0 # ゾロ目数のとき、１ずつ増える
S = 0 # N番目のゾロ目数を代入するための変数

for i in range(1, 555556):

    strI = list(str(i))
    
    # ゾロ目かどうか判定
    check = True
    for j in strI:
        if strI[0] != j:
            check = False
            break
        
    if check:
        x += 1

    # if all(val == strI[0] for val in strI):
    #     x += 1

    if x == N:
        S = i
        break

print(S)