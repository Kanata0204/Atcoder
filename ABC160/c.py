def main():
    k, n = map(int, input().split())
    a_li = list(map(int, input().split()))
    ma = 0
    
    
    
    for i in range(n-1):
        ma = max(ma, a_li[i+1]-a_li[i])
        
    ma = max(ma, k-a_li[n-1]+a_li[0])
        
    print(k - ma)
            
if __name__ == '__main__':
    main()