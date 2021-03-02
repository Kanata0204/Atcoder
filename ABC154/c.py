import collections

def main():
    n = int(input())
    a_li = list(map(int, input().split()))
    
    c = collections.Counter(a_li)
    
    for key, value in c.items():
        if value >= 2:
            exit(print('NO'))
    print('YES')

if __name__ == '__main__':
    main()