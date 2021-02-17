def main():
    n, k = map(int, input().split())
    ans = 0
    li = []
    se = set()
    
    for i in range(n + 1):
        li.append(i)
    
    for i in range(k, len(li)+1):
        mi = sum(li[0:i])
        ma = sum(li[-1*i:])
        kosu = ma - mi + 1
        
        if kosu < 0:
            kosu = 0
            
        ans += kosu
        
    print(ans)
if __name__ == '__main__':
    main()