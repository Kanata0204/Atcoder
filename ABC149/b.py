def main():
    a, b, k = map(int, input().split())
    
    if a+b <= k:
        exit(print(0, 0))
    elif a < k:
        k -= a
        b -= k
        exit(print(0, b))
    else:
        exit(print(a-k, b))
    
    
if __name__ == '__main__':
    main()