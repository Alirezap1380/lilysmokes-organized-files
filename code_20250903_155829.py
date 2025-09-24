def fibonacci(n: int) -> int:
    """Calculate Fibonacci number recursively.

    Args:
        n (int): The position of the Fibonacci sequence to return.

    Raises:
        ValueError: If the input value is not an integer or less than zero.

    Returns:
        int: The Fibonacci number at the given position.
    """
    try:
        if isinstance(n, int) and n >= 0:
            return fibonacci(n - 1) + fibonacci(n - 2) if n > 1 else (n if n == 0 else 1)
        else:
            raise ValueError("Input must be a non-negative integer.")
    except ValueError as e:
        print(f"Error: {e}")