A = []

for _ in range(0, 3):
  row = list(map(int, input().split()))
  A.append(row)
  
check_list = []

for i in range(0, 3):
  row = []
  for j in range(0, 3):
    row.append(False)
    
  check_list.append(row)

n = int(input())

b = []

for i in range(0, n):
  b.append(int(input()))

for i in range(0, 3):
  for j in range(0, 3):
    for k in range(0, n):
      if A[i][j] == b[k]:
        check_list[i][j] = True

###################
# ビンゴかチェック
###################
bingo = False

# 行で揃っているか
for i in range(0, 3):
  if check_list[i][0] and check_list[i][1] and check_list[i][2]:
    bingo = True

# 列で揃っているか
for i in range(0, 3):
  if check_list[0][i] and check_list[1][i] and check_list[2][i]:
    bingo = True

# 左上から右下にかけて揃っているか
if check_list[0][0] and check_list[1][1] and check_list[2][2]:
  bingo = True
  
# 右上から左下にかけて揃っているか
if check_list[0][2] and check_list[1][1] and check_list[2][0]:
  bingo = True

if bingo == True:
  print('Yes')
else:
  print('No')
