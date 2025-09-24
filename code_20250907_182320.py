def add(a: int, b: int) -> int:
    try:
        return a + b
    except TypeError as e:
        raise ValueError("Both arguments should be integers.") from e