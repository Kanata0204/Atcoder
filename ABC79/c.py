def main():
    s = input()
    print(s)
    
    for bit in range(1 << 3):
        print(bit) # 000 ~ 111(0~7)までループする
        ans = int(s[0])
        f = s[0]
        
        for i in range(3):
            if bit&(1 << i): #001 010 100とbitの論理積を求めることでTrueの時だけ+が入ることが分かる
                ans += int(s[i+1])
                f += '+'
            else:
                ans -= int(s[i+1])
                f += '-'
            f += s[i+1]
            
        if ans == 7:
            print(f + "=7")
            exit()
        
if __name__ == '__main__':
    main()