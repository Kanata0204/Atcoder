def main():
    s = input()
    le = len(s)
    
    one_s = s[:(le-1)//2]
    two_s = s[(le+3)//2-1:]
    
    if one_s == one_s[::-1] == two_s == two_s[::-1]:
        print('Yes')
    else:
        print('No')
        
if __name__ == '__main__':
    main()