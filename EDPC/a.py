def main():
    n = int(input())
    h_li = list(map(int, input().split()))
    
    dp = [0] * n
    dp[0] = 0
    dp[1] = abs(h_li[1]-h_li[0])
    
    for i in range(2, n):
        min1 = dp[i-1] + abs(h_li[i] - h_li[i-1])
        min2 = dp[i-2] + abs(h_li[i] - h_li[i-2])
        
        if min1 >= min2:
            dp[i] = min2
        else:
            dp[i] = min1
    
    print(dp[n-1])
    
    
if __name__ == '__main__':
    main()