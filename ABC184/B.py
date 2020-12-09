def main():
    N, X = map(int, input().split())
    S = input().rstrip()
    score = X
    
    for c in S:
        if c == 'o':
            score += 1
        else:
            if score == 0:
                continue
            score -= 1
            
            
    print(score)
    
    
    
    
    
if __name__ == "__main__":
    main()