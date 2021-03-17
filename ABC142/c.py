def main():
    n = int(input())
    a_li = list(map(int, input().split()))
    ans_li = [i for i in range(1, n+1)]
    i = 1
    
    for a in a_li:
        ans_li[a-1] = i
        i += 1
        
    print(' '.join(map(str, ans_li)))
        
        
    
if __name__ == '__main__':
    main()