def main():
    n = int(input())
    s = input()
    ans = ''
    
    for c in s:
        ord_a = ord(c) + n

        if ord_a > 90:
            ord_a -= 26

        ans += chr(ord_a)
        
    print(ans)
    
if __name__ == '__main__':
    main()