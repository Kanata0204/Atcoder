import math

def main():
    k = int(input())
    s = 0
    
    for i in range(1, k + 1):
        for j in range(1, k + 1):
            for l in range(1, k + 1):
                A=math.gcd(i, j)
                s+=math.gcd(A, l)
                
    print(s)
            
if __name__ == '__main__':
    main()