
def main():
    X, Y = map(int, input().split())
    
    if X * 2 <= Y and X * 4 >= Y:
        if Y % 2 == 0:
            print('Yes')
        else:
            print('No')
    else:
        print('No')
    
if __name__ == '__main__':
    main()