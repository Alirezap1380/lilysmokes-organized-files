def multiply(a: int, b: int) -> int:
    try:
        return a * b
    except TypeError:
        raise ValueError("Both arguments must be integers.")