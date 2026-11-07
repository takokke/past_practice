V = 100*10**3 # 最大の合計価値 N(max)*V(max)
N, W = map(int, input().split())
ws = [0] # w0, w1, w2...wNの重さ
vs = [0] # v0, v1, v2...vNの価値

for i in range(N):
    w, v = map(int, input().split())
    vs.append(v)
    ws.append(w)

# weight[i][v] 品物iまで見た上で、価値合計vになるように選んだときの最小の重さ
weight = []
for i in range(N+1):
    weight.append([1<<60]*(V+1))

weight[0][0] = 0

for i in range(1, N+1):
    # 重さws[i], 価値vs[i]である品物iを軸に考える
    for v in range(V+1): # 価値0~10^3の中で、それぞれの場合を考える

        if v - vs[i] >= 0: weight[i][v] = min(weight[i][v], weight[i-1][v-vs[i]]+ ws[i]) # 品物iを選ぶ場合
        weight[i][v] = min(weight[i][v], weight[i-1][v])

result = 0
for v in range(V+1):
    if weight[N][v] <= W: result = v

print(result)