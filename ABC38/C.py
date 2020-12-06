from math import factorial

def main():   
    
    N = int(input())
    s = list(map(int, input().split()))
    
    left = 0
    tmp_left = left
    time = 1
    ans = 0
    
    for right in range(1, N):
        
        if s[right] > s[left]:
            ans += time
            time += 1
        else:
            time = 1
        
        left = right
                
    print(ans + N)
    
if __name__ == '__main__':
    main()