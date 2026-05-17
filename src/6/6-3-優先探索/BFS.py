import queue

# キューの作成
N = 4
Q = queue.Queue()
visited = [] # 訪問済管理
s = 0

key = 4 # goal

values = [10, 21, 3, 4] # グラフの値

# 隣接グラフ
A = [
    [1, 2],  # 0 → 1, 2
    [3],     # 1 → 3
    [3],     # 2 → 3
    []
]

for _ in range(7):
    visited.append(False)

print(visited)

Q.put(s)
visited[s] = True

while Q.qsize() > 0:
    idx = Q.get()
    print(visited)
    for i in A[idx]:
        if not visited[i]:
            Q.put(i)
            visited[i] = True
            print(list(Q.queue))
            if values[i] == key:
                print("発見！" + str(key))
                exit()


