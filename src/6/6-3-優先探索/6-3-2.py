def main():
    import sys
    sys.setrecursionlimit(1000000)

    # グローバルデータ
    H, W = map(int, input().split( ))

    c = []

    visited = []

    sy = 0
    sx = 0
    gx = 0
    gy = 0

    # 入力
    for i in range(H):
        c.append(list(input()))
        visited.append([False] * W)

    for i in range(H):
        for j in range(W):
            if c[i][j] == 's':
                sy = i
                sx = j
            elif c[i][j] == 'g':
                gy = i
                gx = j

    # 幅優先探索
    def dfs(y, x):
        visited[y][x] = True
        for to_y, to_x in [[y-1, x], [y, x+1], [y+1, x], [y, x-1]]:
            if not (0 <= to_y < H and 0 <= to_x < W): # 範囲外
                continue
            if visited[to_y][to_x]: # 訪問済み
                continue
            if c[to_y][to_x] == '#': # 壁は無視
                continue
            dfs(to_y, to_x)
        # 呼び出し元に戻る（親ノードに戻る）

    # 結果の出力
    def printResult():
        if visited[gy][gx]:
            print('Yes')
        else:
            print('No')

    dfs(sy, sx)
    printResult()

main()
