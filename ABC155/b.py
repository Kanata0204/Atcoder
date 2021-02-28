def main():
    n = int(input())
    a_li = list(map(int, input().split()))
    
    for a in a_li:
        if a % 2 == 0:
            if a % 3 != 0 and a % 5 != 0:
                exit(print("DENIED"))
    
    print('APPROVED')
    
if __name__ == '__main__':
    main()
