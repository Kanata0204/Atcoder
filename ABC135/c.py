def main():
    n = int(input())
    a_li = list(map(int, input().split()))
    b_li = list(map(int, input().split()))
    ans = 0
    
    for i in range(n):
        if a_li[i] >= b_li[i]:
            ans += b_li[i]
        else:
            ans += a_li[i]
            mod = b_li[i]-a_li[i]
            
            if mod <= a_li[i+1]:
                a_li[i+1] -= mod
                ans += mod
            else:
                ans += a_li[i+1]
                a_li[i+1] = 0
                
    
    print(ans)
        
    
if __name__ == '__main__':
    main()