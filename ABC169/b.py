def main():
    n = int(input())
    l = list(map(int, input().split()))
    ans = 1
    
    l.sort()
    
    for b in l:
       ans *= b
       
       if 10 ** 18 < ans:
           break
       
    if 10 ** 18 < ans:
        print(-1)
    else:
        print(ans)


if __name__ == '__main__':
    main()