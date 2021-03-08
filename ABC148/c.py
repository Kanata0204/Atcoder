import math

def main():
    a, b = map(int, input().split())
    
    for i in range(2, a):
        print(a * b // math.gcd(a, b))
    
if __name__ == '__main__':
    main()