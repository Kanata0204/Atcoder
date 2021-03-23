import heapq

def main():
    n, m = map(int, input().split())
    A = list(map(lambda x:-int(x) , input().split()))
    heapq.heapify(A)
    
    for i in range(m):
        max_n = heapq.heappop(A)*-1
        max_n //= 2
        heapq.heappush(A, -1*max_n)
    
    print(sum(A)*-1)
    
if __name__ == '__main__':
    main()