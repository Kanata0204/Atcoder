def main():
    n = input()
    le = len(n)
    
    if le == 1:
        exit(print(0))
    
    
    if le % 2 != 0:
        n = '9'*(le-1)
        
    f_block = n[0:le//2]
    t_block = n[le//2:le]
    
    if int(f_block) > int(t_block):
        t_block = '0' * (len(t_block))
    
    if t_block[0] == '0':
        f_block = str(int(f_block)-1)
        t_block = '9' * (len(t_block))
    
    # print(f_block, t_block)
    
    print(min(int(f_block), int(t_block)))
    
    
if __name__ == '__main__':
    main()