def main():
    n = input().rstrip('\r')
    
    hon_l = [2, 4, 5, 7, 9]
    pon_l = [0, 1, 6, 8]
    bon_l = [3]
    
    ans = int(n[-1])
    
    if ans in hon_l:
        print("hon")
    elif ans in pon_l:
        print('pon')
    else:
        print('bon')
    
if __name__ == '__main__':
    main()