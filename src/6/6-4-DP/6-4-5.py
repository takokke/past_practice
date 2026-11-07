N = int(input())

ps = [0] + list(map(int, input().split()))

P = sum(ps)

exist = []

# exist[i][s]:iまでの問題で得点sにできるかどうか真偽値で管理
for i in range(N+1):
    exist.append([False]*(P+1))

# 初期条件
exist[0][0] = True

# iが小さい順にexistの値を求めていく
for i in range(1, N+1):
    for s in range(0, P+1):
        if exist[i-1][s]:
            exist[i][s] = True

        # i問目を解いてsになる場合
        if s >= ps[i] and exist[i-1][s-ps[i]]:
            exist[i][s] = True

ans = 0

# 最後のN問目の列だけ見る
for s in range(P+1):
    if exist[N][s]:
        ans += 1

print(ans)