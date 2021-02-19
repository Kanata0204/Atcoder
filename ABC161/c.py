def main():
    n, k = map(int, input().split())
                
    mo = n % k
    mo_t = (mo - k) * -1
    
    print(min(mo, mo_t))
            
if __name__ == '__main__':
    main()