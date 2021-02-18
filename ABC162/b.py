def main():
    n = int(input())
    ans = 0
    
    for i in range(1, n + 1):
        if 0 != i % 3 and 0 != i % 5:
            ans += i
        
    print(ans)
if __name__ == '__main__':
    main()