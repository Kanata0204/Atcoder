MOD = 10**9 + 7

def main():
    s = input()
    
    old_dp = [0] * 13
    new_dp = [0] * 13
    old_dp[0] = 1
    
    for c in s:
        for i in range(13):
            if c == '?':
                for d in range(10):
                    new_dp[(i * 10 + d) % 13] += old_dp[i]
                    print(new_dp)
            else:
                new_dp[(i * 10 + int(c)) % 13] += old_dp[i]
                print(new_dp)
        
        old_dp = [x % MOD for x in new_dp]
        new_dp = [0] * 13
        print('end', new_dp, old_dp)
        print('============================================')
        
    print(old_dp[5])
    
    
if __name__ == '__main__':
    main()