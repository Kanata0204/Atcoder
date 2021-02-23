def main():
    a, b = map(int, input().split())
    
    ans=-1
    for i in range(10000):
        if a==int(i*0.08) and b==int(i*0.1):
            ans=i
            break
    print(ans)
    
if __name__ == '__main__':
    main()