import math

def main():
    a, b, h, m = map(int, input().split())
    
    angA = 30 * h + 0.5 * m
    angB = 6 * m
    
    angAns = angA - angB

    ans = math.sqrt(a ** 2 + b ** 2 - 2 * a * b * math.cos(math.radians(angAns)))
    
    print(ans)
        
    
    
    
if __name__ == '__main__':
    main()