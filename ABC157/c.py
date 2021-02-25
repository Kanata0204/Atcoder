def main():
    n, m = map(int, input().split())
    ans = []
    
    for a in range(n):
        ans.append(-1)
    
    for i in range(m):
        s, c = map(int, input().split())
        
        if ans[s-1] == -1 or ans[s-1] == c:
            ans[s-1] = c
        else:
            exit(print(-1))
    
    for index, value in enumerate(ans):
        
        if value == -1 and index == 0:
            ans[0] = 1
        elif value == -1:
            ans[index] = 0
            
    ans_n = int("".join(map(str, ans)))
    
    if len(str(ans_n)) == n:
        print(ans_n)
    else:
        print(-1)
    
    
if __name__ == '__main__':
    main()
