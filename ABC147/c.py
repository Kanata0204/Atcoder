def main():
    n = int(input())
    xy_li = []
    
    
    
    for i in range(n):
        for j in range(int(input())):
            xy_li.append(tuple(map(int, input().split())))
            
    print(xy_li)
    
    # 0 : 嘘　1 : 正直
    
    for i in range(1 << n):
        print(i)
if __name__ == '__main__':
    main()