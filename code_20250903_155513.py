def calculator(operation: str, a: float, b: float) -> float:
    """Performs addition, subtraction, multiplication, and division operations on two numbers.

    Args:
        operation (str): The mathematical operation to perform ('+', '-', '*', '/').
        a (float): First number in the operation.
        b (float): Second number in the operation.

    Raises:
        ValueError: If invalid operation is provided.
        TypeError: If non-numeric values are passed for arguments.

    Returns:
        float: Result of the mathematical operation.
    """
    operations = {'+': lambda x, y: x + y, '-': lambda x, y: x - y, '*': lambda x, y: x * y, '/': lambda x, y: x / y}

    try:
        if isinstance(a, (float)) and isinstance(b, (float)):
            return operations[operation](a, b)
        else:
            raise TypeError("Both arguments must be numeric values.")
    except KeyError:
        raise ValueError("Invalid operation provided.")