# https://atcoder.jp/contests/abc165/tasks/abc165_a
K = int(input())
A, B = map(int, input().split())

ok = False

x = A / K
u = B / K

if x < u:
    ok = True

# xとuが同じとき、A(orB)がKの倍数かどうか
if A % K == 0:
    # AとBは同じ
    ok = True

if ok:
    print('OK')
else:
    print('NG')