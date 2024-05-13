N = int(input())
# 配列を返すlistを[]で囲むことによって、２次元配列を作る
# python代入する値を配列にする
S = [list(map(str,input())) for _ in range(N)]

for i in range(N-1, -1, -1):
    if i == N-1:
        continue
    for j in range(1, 2*N-2, 1):
        # S[i][j]が黒く塗られて、Xではない
        if S[i][j] == '#':
            if S[i+1][j-1] == 'X' or S[i+1][j] == 'X' or S[i+1][j+1] == 'X':
                S[i][j] = 'X'
for i in range(0, N, 1):
    print(''.join(S[i]))