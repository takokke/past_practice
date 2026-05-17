# 開始時に、ハードル分を加算する場合


N, L = map(int, input().split(' '))
x = list(map(int, input().split(' ')))

h = [False] * (L+1)

# ハードルの座標
for i in x:
    h[i] = True

T1, T2, T3 = map(int, input().split(' '))

# 動的計画法
# その地点の最小の秒数を記録する
dp = [1000*10**5] * (L+1)
dp[0] = 0

# ちょうどのタイミングでゴールした場合のみ考える
for i in range(1, L+1):
    # 行動を始めた時点でハードル分を追加
    h_cost = 0
    if h[i]:
        h_cost = T3
    
    min_cost = 0
    # 行動1
    min_cost = dp[i-1] + T1
    # 行動2
    if i >=  2:
        min_cost = min(min_cost, dp[i-2] + T1 + T2) # 行動1で終えた場合と、行動2で終えた場合
    # 行動3
    if i >= 4:
        min_cost = min(min_cost, dp[i-4] + T1 + 3*T2) # 行動2で終えた場合と行動3で終えた場合を比較する
    
    # ハードル分のコスト + 求めた最小コスト
    dp[i] = h_cost + min_cost
result = dp[L]

for i in [1, 2, 3]:
    if L-i >= 0:
        result = min(result, dp[L-i]+ (T1 + (i * 2 - 1) * T2) // 2)

print(result)