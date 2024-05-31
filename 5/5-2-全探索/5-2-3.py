# https://atcoder.jp/contests/abc165/tasks/abc165_a

K = int(input())
A,B = input().split()
A = int(A)
B = int(B)

ok = False

for i in range(0, B-A+1, 1):
    flying_distance = A + i
    if flying_distance % K == 0:
        ok = True
        break

if ok:
    print('OK')
else:
    print('NG')   