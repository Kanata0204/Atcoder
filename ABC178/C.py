def main():
    N = int(input())

    mod = 10**9 + 7
    ans = pow(10, N, mod) - 2*pow(9, N, mod) + pow(8, N, mod)
    print(ans % mod)


if __name__ == "__main__":
    main()
