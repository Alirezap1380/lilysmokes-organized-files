def calculate_circle_area(radius: float) -> float:
    try:
        return 3.14 * radius ** 2
    except TypeError as e:
        raise ValueError("Radius must be a floating point number.") from e