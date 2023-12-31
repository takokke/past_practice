num = int(input())
a = list(map(int, input().split()))
even = True
count = 0

while (even):
  for i in range(0, num):
    if a[i] % 2 == 0:
      a[i] /= 2
    else:
      even = False
  if (even):
    count += 1
print(count)