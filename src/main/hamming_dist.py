def hamming_dist(lhs: str, rhs: str) -> int:
    """hamming_dist computes the hamming distance between two sequences.
    Tha hamming distance is the number of position in which two sequences differ.

    Args:
        lhs (str): first DNA sequence
        rhs (str): second DNA sequence

    Returns:
        int: count of positions in which the sequences differ.
    """
    return len([(x, y) for x, y in zip(lhs, rhs) if x != y])
