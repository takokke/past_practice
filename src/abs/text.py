N = int(input())
A = list(map(int, input().split()))
count = 0
ok = True

while ok:
    for num in A:
        if num % 2 != 0 and not isinstance(num / 2, int):
            ok = False
            break
    if ok:
        A = list(map(lambda x: int(x / 2), A))
        count+=1

print(count)