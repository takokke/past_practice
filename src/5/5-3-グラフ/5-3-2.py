N, M, Q = map(int,input().split())
graph = [[] for _ in range(N)]

# 隣接リストを作成
for _ in range(M):
    u, v = map(int, input().split())
    graph[u-1].append(v)
    graph[v-1].append(u)

C = list(map(int, input().split()))

for _ in range(Q):
    query = list(map(int, input().split()))
    type = query[0]
    x = query[1] - 1
    if type == 1:
        print(C[x])
        for i in range(len(graph[x])):
            next = graph[x][i] - 1
            C[next] = C[x]

    elif type == 2:
        print(C[x])
        y = query[2]
        C[x] = y

