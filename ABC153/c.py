def main():
    n, k = map(int, input().split())
    h_li = list(map(int, input().split()))
    
    if k > len(h_li):
        k = len(h_li)
    
    h_li.sort()
    
    for i in range(k):
        h_li.pop()
        
    print(sum(h_li))

if __name__ == '__main__':
    main()