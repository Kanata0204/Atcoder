def main():
    x = int(input())
    s = 100
    ans = 0
    
    while(x > s):
        s += (s // 100)
        ans += 1
        
    print(ans)
    
if __name__ == '__main__':
    main()