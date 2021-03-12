a, b, x = map(int, input().split())

def cost(n):
    return a * n + b * len(str(n))

def main():
    bottom = 1
    top = 10**9
    
    if cost(1) > x:
        exit(print(0))
    
    if cost(10**9)  <= x:
        exit(print(10**9))
        
    while(top-bottom > 1):
        mid = (top + bottom) // 2
        if cost(mid) <= x:
            bottom = mid
        else:
            top = mid
            
    print(bottom)
    
if __name__ == '__main__':
    main()