def main():

    try:
        N = input()

        a = list(N)
        s = 0

        for i in range(len(a)):
            s += int(a[i])

        print("Yes" if s % 9 == 0 else "No")

    except EOFError:
        print("No")


if __name__ == "__main__":
    main()
