import math
import itertools

def distance(xi, xj, yi, yj):
    return math.sqrt((xi-xj)**2 + (yi-yj)**2)

def main():
    n = int(input())
    xy_li = [tuple(map(int, input().split())) for i in range(n)]
    ans = 0
    
    ptns = itertools.permutations(xy_li)
    
    for v in ptns:
        for i in range(len(v)-1):
            ans += distance(v[i][0], v[i+1][0], v[i][1], v[i+1][1])
        
    print(ans / math.factorial(n))


if __name__ == '__main__':
    main()