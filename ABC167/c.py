def main():
    n, m, x = map(int, input().split())
    inp = [list(map(int, input().split())) for _ in range(n)]
    
    ans = 10**18
    
    for i in range(1 << n):
        tmp_ans = 0
        check = [0] * m
        
        for j in range(n):
            if i & (1 << j):
                tmp_ans += inp[j][0]
                for k in range(m):
                    check[k] += inp[j][k + 1]
                    
        if all([j >= x for j in check]):
                ans = min(ans, tmp_ans)
                
    if ans == 10**18:
        print(-1)
    else:
        print(ans)
        
if __name__ == '__main__':
    main()