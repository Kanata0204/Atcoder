import math


def main():
    n = int(input())
    print(math.ceil(n/1000)*1000 - n)


if __name__ == "__main__":
    main()
