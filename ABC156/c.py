def main():
    n = int(input())
    x_li = list(map(int, input().split()))
    s = 0
    ans = 10**9
    
    for p in range(1, 101):
        
        for x in x_li:
            s += (x-p) ** 2
        
        if ans > s:
            ans = s
        s = 0
        
    print(ans)
    
if __name__ == '__main__':
    main()
