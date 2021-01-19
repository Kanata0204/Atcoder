
def main():
    N, K = map(int, input().split())
    p = list(map(int, input().split()))
    s = 0
    
    p.sort()
    
    for i in range(K):
        s += p.pop(0)
    
    print(s)

if __name__ == '__main__':
    main()