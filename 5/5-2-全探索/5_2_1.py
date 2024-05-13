import math

N = int(input())

# ゾロ目数の桁数
x = math.ceil(N / 9)

# N番目のゾロ目数の数字
y = N % 9
if y == 0:
  y = 9

ans = ''

for _ in range(0, x):
  ans = ans + str(y)
  
print(ans)

