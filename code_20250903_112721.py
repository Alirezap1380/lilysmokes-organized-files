def fibonacci(n: int = 10) -> list:
    try:
        sequence = [0, 1]
        while len(sequence) < n:
            next_number = sum(sequence[-2:])
            sequence.append(next_number)
        return sequence
    except ValueError:
        print("Invalid input. Please provide an integer greater than or equal to 0.")