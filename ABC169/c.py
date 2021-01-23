from decimal import Decimal

def main():
    a, b = map(Decimal, input().split())
    print(int(a*b))

if __name__ == '__main__':
    main()