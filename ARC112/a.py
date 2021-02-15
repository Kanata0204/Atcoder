import math

def main():
    t = int(input())
    li = [list(map(int, input().split())) for _ in range(t)]
    ans = 0
    
    for l in li:
        sa = l[1] - l[0]
        
        if l[0] > sa:
            print(0)
            continue
        
        for j in range(sa-l[0]+1):
            ans += j+1
            
        print(ans)
            
    
if __name__ == '__main__':
    main()