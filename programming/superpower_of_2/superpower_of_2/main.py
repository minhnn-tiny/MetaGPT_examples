def super_power(n: int) -> int:
    """
    Calculates the SuperPower of 2, which is 2^n mod 1000000007.

    Args:
        n (int): The exponent of 2.

    Returns:
        int: The SuperPower of 2.
    """

    return pow(2, n, 1000000007)


if __name__ == "__main__":
    n = int(input())
    print(super_power(n))
