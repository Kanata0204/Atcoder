from itertools import accumulate

def main():
    N, M, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    
    accum_a = [0] + list(accumulate(A))
    accum_b = [0] + list(accumulate(B))
    
    ans = 0
    j = M
    
    for i in range(N+1):
        if accum_a[i] > K:
            break
        while(K - accum_a[i] < accum_b[j]):
            j -= 1
        ans = max(ans, i + j)
        
    
    print(ans)

if __name__ == '__main__':
    main()