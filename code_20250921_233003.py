def add_numbers(a: int, b: int) -> int:
    try:
        return a + b
    except TypeError as e:
        print(f"Error: {e}. Both arguments should be integers.")
        return None