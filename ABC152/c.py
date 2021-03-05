def main():
    n = int(input())
    p_li = list(map(int, input().split()))
    min = p_li[0]
    ans = 1
    
    for p in p_li:
        
        if min > p:
            min = p
            ans += 1
            
    print(ans)
    
if __name__ == '__main__':
    main()