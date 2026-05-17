def std_input():
    N, K  = map(int, input().split())
    h = list(map(int, input().split()))
    return N, K, h

def DP(N: int, K:int, h: list[int]) -> int:
    cost = [0] * N

    for i in range(1, N):
        min_cost = 10000000000
        for j in range(1, K+1):
            if i - j < 0:
                break
            min_cost = min(min_cost, cost[i-j] + abs(h[i]-h[i-j]))
        
        cost[i] = min_cost
    
    return cost[N-1]


def main():
    N, K, h = std_input()
    result = DP(N, K, h)
    print(result)


if __name__ == '__main__':
    main()