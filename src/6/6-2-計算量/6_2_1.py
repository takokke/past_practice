N = int(input())
C = list(map(int, input().split()))
Q = int(input())

# セット売りの最小値
min_s_c = 10000000000
# 全販売の最小値
min_z_c = 10000000000

# セット販売の合計数
s = 0

# 全販売数
z = 0

# 販売枚数
sell = 0

# 最小値を求める
for i in range(N):
    if (i+1) % 2 == 1:
        min_s_c = min(min_s_c, C[i])
        
    else:
        min_z_c = min(min_z_c, C[i])

for i in range(Q):
    S =  list(map(int, input().split()))

    # 単品販売
    if S[0] == 1:
        x = int(S[1])
        a = int(S[2]) # xの販売枚数

        # 販売後のカードxの在庫を求める
        if x % 2 == 1:
            card_x = C[x-1] - z - s - a  # 奇数の場合
        else:
            card_x = C[x-1] - z - a

        # カードxの在庫が足りる場合
        if card_x >= 0:
            # 在庫数の更新
            C[x-1] -= a
            # 販売枚数の更新
            sell += a
            
            if x % 2 == 1:
                min_s_c = min(min_s_c, C[x-1])
            else:
                min_z_c = min(min_z_c, C[x-1])

    elif S[0] == 2: # セット販売
        a = int(S[1])
        if min_s_c - s - z - a >= 0:
            # min_s_c -= a
            # min_z_c = min(min_z_c, min_s_c)
            s += a
            
    elif S[0] == 3: # 全販売
        a = int(S[1])
        if min(min_s_c - s - z - a, min_z_c - z - a) >= 0:
            # min_z_c -= a
            # min_s_c -= a
            z += a
    # print(S)
    # print(C)
    # print("s = "+str(s))
    # print("z = "+str(z))
    # print("min_z_c = " + str(min_z_c))
    # print("min_s_c = " + str(min_s_c))
    # print("sell = "+ str(sell))
    # print("------------------------------------------------------")

for i in range(N):
    sell += z
    if (i+1)%2 == 1:
        sell += s

print(sell)