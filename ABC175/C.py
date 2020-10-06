def main():
    X, K, D = map(int, input().split())
    X = abs(X)
    rem = K

    cnt = min(X // D, K)
    X -= D*cnt
    rem -= cnt

    if rem > 0:
        if rem % 2 == 1:
            X = X - D

    print(abs(X))


if __name__ == "__main__":
    main()
