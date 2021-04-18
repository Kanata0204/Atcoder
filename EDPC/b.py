def main():
    n, k = map(int, input().split())
    h_li = list(map(int, input().split()))
    
    dp = [0] * n
    dp[0] = 0
    
    for i in range(1, n):
        pre_dp = 10**9
        for j in range(min(i, k)):
            
            pre = dp[i-(j+1)]+abs(h_li[i-(j+1)]-h_li[i])
            
            if pre < pre_dp:
                pre_dp = pre
                
            
        dp[i] = pre_dp
            
    print(dp[n-1])
    
if __name__ == '__main__':
    main()