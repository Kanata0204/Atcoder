import collections

def main():
    n = int(input())
    a_li = list(map(int, input().split()))
    
    c = collections.Counter(a_li)
    
    for i in range(1, n+1):
        print(c[i])
        
    
if __name__ == '__main__':
    main()