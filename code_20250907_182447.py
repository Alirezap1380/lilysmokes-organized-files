def divide(a: float, b: float) -> float:
    try:
        return a / b
    except ZeroDivisionError:
        raise ValueError("Cannot divide by zero")