def main():
    n = int(input())
    s = input()
    tmp = ''
    cnt = 0
    
    for c in s:
        if tmp == c:
            continue
        cnt += 1
        tmp = c
        
    print(cnt)
if __name__ == '__main__':
    main()