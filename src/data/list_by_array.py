from array import array
import time

N = 1000000
arr1 = array('i', [0]*N)
for i in range(N):
    arr1[i] = i+1

# 末尾に要素を追加する
start = time.perf_counter()
arr2 = array('i', [0]*(N+1))
for i in range(N):
    arr2[i] = arr1[i]
arr2[N] = 1
end = time.perf_counter()
print(round((end - start)*1000, 10), "m秒")
