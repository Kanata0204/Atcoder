def main():
    n, a, b = map(int, input().split())
    
    loop = n // (a + b)
    mod = n % (a + b)
    ans = a * loop
    
    print(ans + min(mod, a))
    
if __name__ == '__main__':
    main()