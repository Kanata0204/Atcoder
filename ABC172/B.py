def main():
    cnt = 0
    s1 = input().rstrip()
    s2 = input().rstrip()
    
    s3 = zip(s1, s2)
    

    for c1, c2 in s3:
        if c1 != c2:
            cnt += 1
            
    print(cnt)


if __name__ == '__main__':
    main()