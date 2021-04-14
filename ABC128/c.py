def main():
    n, m = map(int, input().split())
    s_li = [list(map(int, input().split())) for _ in range(m)]
    
    for i in range(m):
        s_li[i].pop(0)
    
    p_li =list(map(int, input().split()))
    flag = [0] * m
    hits = [0] * m
    
# 00, 01, 10, 11...スイッチ全探索
    for i in range(1 << n):
        # 1, 10, 100...どのスイッチがonか?
        for j in range(n):
            x = 2 ** j
            # もしもonだったら
            if i & x:
                # 
                for k in range(m):
                    if j + 1 in s_li[k]:
                        hits[k] += 1
    
    # for i in range(0, n+1, 2):
    #     print(i)
                
    print(k_s_li, p_li, flag)
    
if __name__ == '__main__':
    main()