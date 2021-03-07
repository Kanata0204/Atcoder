def main():
    x = int(input())
    
    while(True):
        
        for i in range(2, x):
            if x % i == 0:
                break
        else:
            exit(print(x))
            
        x += 1
    
if __name__ == '__main__':
    main()