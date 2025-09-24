def fibonacci(n: int) -> int:
    """
    Returns the nth number in the Fibonacci sequence.

    Args:
        n (int): The position of the number to return in the Fibonacci sequence.
            Starts at 0 for the first number (0), and increments by 1 for each subsequent number.

    Raises:
        ValueError: If the input value is not a valid integer.

    Examples:
        >>> fibonacci(0)
        0
        >>> fibonacci(1)
        1
        >>> fibonacci(2)
        1
        >>> fibonacci(3)
        2
        >>> fibonacci(13)
        89
    """
    if not isinstance(n, int):
        raise ValueError("Input must be an integer.")
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")

    fib_sequence = [0, 1]
    if n > 1:
        for i in range(2, n + 1):
            fib_sequence.append(fib_sequence[i - 1] + fib_sequence[i - 2])
    return fib_sequence[n]