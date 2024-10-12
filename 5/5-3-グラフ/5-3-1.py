# https://atcoder.jp/contests/past202005-open/tasks/past202005_e

N, M, Q = map(int,input().split())
graph = [[False for i in range(N)] for j in range(N)  ] # ui、viを追加する隣接行列

for i in range(M):
    u, v = map(int, input().split())
    graph[u-1][v-1] = True
    graph[v-1][u-1] = True
    
C = list(map(int, input().split())) # 色の取得

# クエリを取得し実行する
for i in range(Q):
    s = list(map(int, input().split()))
    # クエリの場合分け
    if s[0] == 1:
        x = s[1] - 1
        print(C[x])
        # スプリンクラー
        for j in range(N):
            if graph[x][j] == True:
                C[j] = C[x]
    elif s[0] == 2:
        x = s[1] - 1
        y = s[2]
        print(C[x])
        # 塗り替え
        C[x] = y