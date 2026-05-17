def main():
    N, L = map(int, input().split())
    
    x = list(map(int, input().split()))
    
    # 配列に値が含まれるかの書き方だと、遅くなるため
    # 例 if i in x:
    hurdles = [False] * (L+1)
    for i in x:
        hurdles[i] = True
    
    T1, T2, T3, = map(int, input().split())
    
    # 動的計画法でコストを記録
    dp = [0] * (L+1)
    for i in range(1, L+1):
        # 行動1のみ
        if i <= 1:
            dp[i] = T1
        elif i <= 3:
        # 行動1 or 行動2
            dp[i] = min(dp[i-1] + T1, dp[i-2] + T1 + T2)
        else:
        # 行動1 or 行動2 or 行動3
            dp[i] = min(dp[i-1] + T1, dp[i-2] + T1 + T2, dp[i-4] + T1 + 3*T2)
        
        if hurdles[i]:
            dp[i] += T3
    
    ans = dp[L]
    
    # #　残りの距離1
    # if L-1 >= 0:
    #   ans = min(ans, dp[L-1] + int(T1/2) + int(T2/2))
    # # 残りの距離2
    # if L-2 >= 0:
    #   ans = min(ans, dp[L-2] + int(T1/2) + int(1.5*T2))
    # # 残りの距離3
    # if L-3 >= 0:
    #   ans = min(ans, dp[L-3] + int(T1/2) + int(2.5*T2))
        
    for i in [1, 2, 3]:
        if L - i >= 0:
            ans = min(ans, dp[L-i] + T1//2 + T2*(2*i-1)//2)
    print(ans)

if __name__ == "__main__":
    main()