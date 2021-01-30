def main():
    n, s, d = map(int, input().split())
    
    a = [list(map(int, input().split())) for i in range(n)]
    
    
    for i in range(len(a)):
        if a[i][0] < s and a[i][1] > d:
            exit(print('Yes'))
    
    print('No')
            
    
    
if __name__ == '__main__':
    main()