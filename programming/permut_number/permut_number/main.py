def main():
    """
    The main function.
    """
    a, b = map(int, input().split())
    count = 0
    for i in range(a, b + 1):
        permut_number = PermutNumber(i)
        if permut_number.is_permut():
            count += 1
    print(count)


if __name__ == "__main__":
    main()
