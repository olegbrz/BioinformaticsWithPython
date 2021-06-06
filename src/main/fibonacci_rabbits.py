def fibonacci_rabbits(n: int) -> int:
    """fibonacci_rabbits computes the number of rabbit pairs that will be
       present after n months.

    Args:
        n (int): months number.

    Returns:
        int: number of rabbit pairs after n months.
    """
    if n < 0:
        raise ValueError("Months number should be equal or greater than 0.")
    parent = 1
    child = 1
    for _ in range(n):
        child, parent = parent, parent + child
    return child
