def main():
    K = int(input())
    s = input()
    
    le = len(s)
    
    if le > K:
        exit(print(s[:K] + '...'))
    else:
        print(s)

if __name__ == "__main__":
    main()