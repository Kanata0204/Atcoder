def main():
    N = int(input())
    a = list(map(int, input().split()))

    DP = [0] * N
    max_i = 0

    for i in range(1, N):
        if a[max_i] > a[i]:
            DP[i] += (a[max_i]-a[i])
        elif a[max_i] < a[i]:
            max_i = i

    print(sum(DP))


if __name__ == "__main__":
    main()
