def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    ppr = []
    
    s = sum(a)
    a.sort()
    
    for i in range(m):
        if a.pop() < s / (4 * m):
            exit(print('No'))
            
    print('Yes')
    
if __name__ == '__main__':
    main()