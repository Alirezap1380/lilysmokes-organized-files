def square_number(number: float) -> float:
    try:
        return number ** 2
    except TypeError as e:
        raise ValueError("Input must be a numeric type.") from e