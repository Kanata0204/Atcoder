def main():
    #尺取り法
     
    N,K = map(int,input().split())
    s = [int(input()) for i in range(N)]
    ans = 0
    
    seki = 1
    left = 0
    ans = 0
    tmplen = 0
     
    if 0 in s:
        print(len(s))
        exit()
     
    for right in range(N):
        seki *= s[right]
        
        if seki > K and left == right:
            left += 1
            seki = 1
            continue
        
        tmplen += 1
        
        while(seki > K):
            seki //= s[left]
            left += 1
            tmplen -= 1
        
        ans = max(ans, tmplen)
       
     
    print(ans)
    
if __name__ == '__main__':
    main()