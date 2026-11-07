N, W = map(int, input().split())
ws = [0] # w0, w1, w2...wNの重さ
vs = [0] # v0, v1, v2...vNの重さ

for i in range(N):
    w, v = map(int, input().split())
    vs.append(v)
    ws.append(w)

# value[i][w] 品物iまで見た上で、重さ合計wになるように選んだときの最大の価値
value = []
for i in range(N+1):
    value.append([-1]*(W+1))

value[0][0] = 0

for i in range(1, N+1):
    # 重さws[i], 価値vs[i]である品物iを軸に考える
    for w in range(W+1): # 重さ0~Wの中で、それぞれの場合を考える
        value[i][w] = value[i-1][w]
        if w - ws[i] < 0: continue
        value[i][w] = max(value[i][w], value[i-1][w-ws[i]] + vs[i])

result = max(value[N])
print(result)