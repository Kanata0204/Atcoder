def main():
    k = int(input())
    a, b = map(int, input().split())
    
    waru = b // k
    
    print("OK" if waru * k >= a else "NG")
        
if __name__ == '__main__':
    main()