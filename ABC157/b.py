def main():
    bingo_li = [list(map(int, input().split())) for _ in range(3)]
    n = int(input())
    
    for _ in range(n):
        inp = int(input())
        
        for row in bingo_li:
            
            for i in range(3):
                if inp == row[i]:
                    row[i] = -1
           
           
    for i in range(3):
        if bingo_li[0][i] == bingo_li[1][i] == bingo_li[2][i] == -1 or bingo_li[i][0] == bingo_li[i][1] == bingo_li[i][2] == -1 or bingo_li[0][0] == bingo_li[1][1] == bingo_li[2][2] == -1 or bingo_li[0][2] == bingo_li[1][1] == bingo_li[2][0] == -1:
            exit(print('Yes'))
        
    print('No')
    
if __name__ == '__main__':
    main()