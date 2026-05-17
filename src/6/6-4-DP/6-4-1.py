def std_input():
    N = int(input())
    h = list(map(int, input().split()))
    return N, h

def DP(N: int, h: list[int]) -> int:
    cost = [0] * N
    cost[1] = cost[0] + abs(h[0]-h[1])

    for i in range(2, N):
        cost[i] = min( cost[i-2] + abs(h[i]-h[i-2]), cost[i-1] + abs(h[i]-h[i-1]))

    return cost[N-1]


def main():
    N, h = std_input()
    result = DP(N, h)
    print(result)


if __name__ == '__main__':
    main()