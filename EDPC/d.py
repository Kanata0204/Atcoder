def main():
    N, W = map(int, input().split())
    dp = [[0 for _ in range(W+1)] for _ in range(N+1)]
    
    for i in range(1, N+1):
        w, v = map(int, input().split())
        
        for j in range(W+1):
            if j >= w:
                dp[i][j] = max(dp[i-1][j - w] + v, dp[i-1][j])
            else:
                dp[i][j] = dp[i-1][j]
    
    print(dp[-1][-1])
    
if __name__ == '__main__':
    main()