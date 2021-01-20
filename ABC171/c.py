
def main():
    N = int(input())
    t = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
    a = ''
    
    while(N > 0):
        n = N % 26
        a = t[n-1] + a
        N //= 26
        if n == 0:
            N -= 1
    
    print(a)
    
        
if __name__ == '__main__':
    main()