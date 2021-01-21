
def main():
    x, n = map(int, input().split())
    p = list(map(int, input().split()))
    
    for i in range(n + 1):
        for j in [-1, 1]:
            if p.count(x + j * i) == 0:
                print(x + j * i)
                exit()
            
        

if __name__ == '__main__':
    main()