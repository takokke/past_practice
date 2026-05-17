from collections import deque

Q = deque()

R, C = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())

c = [] # 二次元盤面

for i in range(R):
    row = list(input())
    c.append(row)

# 1始まりの入力を0にする
sy -= 1
sx -= 1
gy -= 1
gx -= 1


dist = []
for i in range(R):
    dist.append([-1]*C)

Q.append([sy, sx])
dist[sy][sx] = 0 # 移動回数

while len(Q) > 0:
    i, j = Q.popleft()
    for i2, j2 in [[i-1, j], [i, j+1], [i+1, j], [i, j-1]]:
        if not (0 <= i2 < R and 0<= j2 < C): # 範囲外の場合
            continue
        if c[i2][j2] == '#': # 壁の場合
            continue
        if dist[i2][j2] != -1: # 訪問している場合
            continue
        dist[i2][j2] = dist[i][j] + 1 # 移動回数の更新
        Q.append([i2, j2])

print(dist[gy][gx])
