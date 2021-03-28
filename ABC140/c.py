def main():
    n = int(input())
    b_li = list(map(int, input().split()))
    ans = b_li[0] + b_li[len(b_li)-1]
    
    for i in range(len(b_li)-1):
        ans += min(b_li[i], b_li[i+1])
        
    print(ans)
    
if __name__ == '__main__':
    main()