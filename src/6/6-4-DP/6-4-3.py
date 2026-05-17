# メモ化再帰

import sys
sys.setrecursionlimit(10**5)

N = int(input())
h = list(map(int, input().split()))
h.insert(0, 0)
dp = [0] * (N+1)
checked = [False] * (N+1) 

def rec(i):
    if checked[i]:
        return dp[i]
    if i == 2:
        dp[2] = abs(h[2]-h[1])
    elif 2 < i:
        min_cost = min(rec(i-1) + abs(h[i]-h[i-1]), rec(i-2) + abs(h[i] - h[i-2]))
        dp[i] = min_cost

    checked[i] = True
    return dp[i]

result = rec(N)
print(result)