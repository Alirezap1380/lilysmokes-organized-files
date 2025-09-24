def multiply(a: int | float, b: int | float) -> int | float:
    """
    Multiplies two numbers and returns their product.

    :param a: First number to be multiplied.
    :type a: int or float
    :param b: Second number to be multiplied.
    :type b: int or float
    :return: The product of the two numbers.
    :rtype: int or float
    """
    try:
        return a * b
    except TypeError as e:
        print(f'Error: {e}')