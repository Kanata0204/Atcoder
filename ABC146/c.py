def main():
    a, b, x = map(int, input().split())
    pre_n = 1
    pre_i = 1
    
    print(a, b,x)
    
    if (a >= 10**9 or b >= 10**9) and x >= 10 ** 9:
        exit(print(10**9))
    
    while(True):
        s = a * pre_n + b * pre_i
        print('s:',pre_i,  s)
        
        if s > x:
            # print(s, pre_i, pre_n)
            break
    
        pre_i += 1
        pre_n *= 10
        
    s -= a + b # pre_i -= 1
    # print(s)
    pre_i -= 1
    print('s-x', s-x)
    syo = (s - x) // a + 1
    print(syo)
    tmp = s - a * syo
    print(tmp)
    
    # print(s, len(str(s)))
    print(pre_i)
    
    # print('---------------')
    
    if s <= x:
        exit(print((tmp-(b*pre_i))//a))
    elif s - a * ((s - x) // a + 1) > 10**9:
        print(10**9)
    else:
        syo = (s - x) // a + 1
        # print(syo)
        # print(s-x)
        # print((s - x) // a)
        # print((s - x) // a + 1)
        # print(a * syo)
        tmp = s - a * syo
        # print(tmp)
        print((tmp-(b*pre_i))//a)
        
    
if __name__ == '__main__':
    main()