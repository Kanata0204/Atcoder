def main():
    x = int(input())
    
    ans_gohya = x // 500
    ans_go = (x - (ans_gohya * 500)) //5
    
    print(ans_gohya*1000 + ans_go*5)
            
if __name__ == '__main__':
    main()