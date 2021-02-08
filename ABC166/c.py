def main():
    n, m = map(int, input().split())
    hl = list(map(int, input().split()))
    ans = [1] * n
    
    loads = [list(map(int, input().split())) for _ in range(m)]
    
    for load in loads:
        
        if hl[load[0]-1] > hl[load[1]-1]:
            ans[load[1]-1] = 0
            
        elif hl[load[0]-1] < hl[load[1]-1]:
            ans[load[0]-1] = 0
        
        else:
            ans[load[0]-1] = 0
            ans[load[1]-1] = 0
        
    print(sum(ans))
        
if __name__ == '__main__':
    main()