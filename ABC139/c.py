def main():
    n = int(input())
    h_li = list(map(int, input().split()))
    tmp = 0
    ans = 0
    
    for i in range(len(h_li)-1):
        if h_li[i] >= h_li[i+1]:
            tmp += 1
            # print(h_li[i], h_li[i+1], tmp)
        else:
            # print(h_li[i], h_li[i+1], ans, tmp)
            if tmp > ans:
                ans = tmp
            tmp = 0
            
    else:
        if tmp > ans:
            ans = tmp
            tmp = 0
            
    print(ans)        
        
    
if __name__ == '__main__':
    main()