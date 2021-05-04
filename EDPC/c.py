def main():
    n = int(input())
    
    a = [0] * (n+1)
    b = [0] * (n+1)
    c = [0] * (n+1)
    
    for i in range(1, n+1):
        a[i], b[i], c[i] = map(int, input().split())
        
    # 各日の最大幸福度を入れる
    dp = [[0] * 3 for _ in range(n + 1)]
    
    for i in range(n+1):
        if i == 1:
            dp[1][0] = a[1]
            dp[1][1] = b[1]
            dp[1][2] = c[1]
        else:
            dp[i][0] = max(dp[i-1][1] + a[i], dp[i-1][2] + a[i])
            dp[i][1] = max(dp[i-1][0] + b[i], dp[i-1][2] + b[i])
            dp[i][2] = max(dp[i-1][0] + c[i], dp[i-1][1] + c[i])
    
    print(max(dp[n][0], dp[n][1], dp[n][2]))
    
if __name__ == '__main__':
    main()