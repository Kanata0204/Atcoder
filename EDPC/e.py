MAX_N = 100
MAX_V = 1000

def main():
    N, W = map(int, input().split())
    
    wv = [list(map(int, input().split())) for _ in range(N)]
    
    dp = [[10**9+1 for _ in range(MAX_N * MAX_V + 1)] for _ in range(N + 1)]
    dp[0][0] = 0
    
    # print(wv[i-1][0])
    
    for i in range(1, N+1):
        w = wv[i-1][0]
        v = wv[i-1][1]
        
        for j in range(MAX_N * MAX_V + 1):
            if j >= v:
                dp[i][j] = min(dp[i-1][j], dp[i-1][j-v] + w)
            else:
                dp[i][j] = dp[i-1][j]
                
    # print(dp[1])
                
    for i in reversed(range(MAX_N * MAX_V + 1)):
        if dp[N][i] <= W:    
            print(i)
            exit()
    
if __name__ == '__main__':
    main()