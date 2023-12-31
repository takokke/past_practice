C = []
check = True

for _ in range(0, 3):
  row = list(map(int, input().split()))
  C.append(row)

if not C[0][0] - C[0][1] == C[1][0] - C[1][1] == C[2][0] - C[2][1]:
  check = False
  
if not C[0][1] - C[0][2] == C[1][1] - C[1][2] == C[2][1] - C[2][2]:
  check = False
  
if not C[0][0] - C[1][0] == C[0][1] - C[1][1] == C[0][2] - C[1][2]:
  check = False
  
if not C[1][0] - C[2][0] == C[1][1] - C[2][1] == C[1][2] - C[2][2]:
  check = False
  
if check:
  print('Yes')
else:
  print('No')