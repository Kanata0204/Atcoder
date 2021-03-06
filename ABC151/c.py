import itertools

def main():
    n = int(input())
    p_li = input().split()
    q_li = input().split()
    p_li_s = sorted(p_li)
    li = list(itertools.permutations(p_li_s))
    
    p_li = tuple(p_li)
    q_li = tuple(q_li)
    
    ans = (li.index(p_li) + 1) - (li.index(q_li) + 1)
    
    if ans < 0:
        ans *= -1
    
    print(ans)
    
    
if __name__ == '__main__':
    main()