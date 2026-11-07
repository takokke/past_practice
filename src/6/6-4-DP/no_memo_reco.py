import time
import sys
sys.setrecursionlimit(20)
max = 50
cnt = [0] * (max+1)

def calc_fibo(N):
    cnt[N] = cnt[N] + 1
    if N == 1: return 1
    if N == 0: return 0

    return calc_fibo(N-1) + calc_fibo(N-2)

def main():
    start = time.perf_counter()
    result = calc_fibo(max)
    end = time.perf_counter()
    # for i in range(max+1):
    #     print(f"calc_fibo({i}) : {cnt[i]}回呼ばれました")
    print(f"フィボナッチ数列の{max}番目までの合計は{result}です")

    print(round((end - start)*1000, 10), "m秒")

if __name__ == '__main__':
    main()