def main():
    n = int(input())
    h_li = list(map(int, input().split()))
    
    for i in range(1, n):
        
        if h_li[i] - h_li[i-1] >= 1:
            h_li[i] -= 1
        elif h_li[i] - h_li[i-1] == 0:
            continue
        else:
            exit(print('No'))
            
            
    print('Yes')
            
        
    
if __name__ == '__main__':
    main()