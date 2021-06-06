from typing import List


def k_mer(dna: str, k: int) -> List[str]:
    """k_mer computes all existing k-mers in a sequence.

    Args:
        dna (str): DNA sequence
        k (int): k parameter for k-mer

    Returns:
        List[str]: list of all existing k-mers
    """
    return [dna[i:i+k] for i in range(len(dna)-k+1)]
