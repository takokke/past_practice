C = []
A = []
B = []
check = True

for _ in range(0, 3):
  row = list(map(int, input().split()))
  C.append(row)
  
# a1は好きな数値で固定
a1 = 1

# b123を求める
b1 = C[0][0] - a1
b2 = C[0][1] - a1
b3 = C[0][2] - a1

B.append(b1)
B.append(b2)
B.append(b3)

# a2を求める
a2 = C[1][0] - b1

# a3を求める
a3 = C[2][0] - b1

A.append(a1)
A.append(a2)
A.append(a3)

for i in range(0, 3):
  for j in range(0, 3):
    if not A[i] + B[j] == C[i][j]:
      check = False
      
if check:
  print('Yes')
else:
  print('No')