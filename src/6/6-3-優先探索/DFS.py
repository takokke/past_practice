N = 5
s= 0
visited = []
E = [
    [1, 2],
    [3],
    [3, 4],
    [],
    []
]
for _ in range(N):
    visited.append(False)

def dfs(i) :
    # 訪問済み処理
    visited[i] = True
    print(str(i) + "を訪問しました")
    print(visited)
    for j in E[i]:
        if not visited[j]: # 訪問済みでなければ
            dfs(j)

dfs(s)