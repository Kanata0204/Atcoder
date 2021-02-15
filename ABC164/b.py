def main():
    a, b, c, d = map(int, input().split())
    
    while(True):
        c -= b
        if c <= 0:
            exit(print('Yes'))
        
        a -= d
        if a <= 0:
            exit(print('No'))
    
if __name__ == '__main__':
    main()