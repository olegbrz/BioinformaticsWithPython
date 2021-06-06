from collections import Counter
from typing import List, Tuple


def motifs(dna: str, k: int, n: int = 5) -> List[Tuple(str, int)]:
    """motifs calculates the most common k-mers in a sequence.

    Args:
        dna (str): DNA sequence
        k (int): k-mer k parameter
        n (int, optional): number of top results to return. Defaults to 5.

    Returns:
        List[Tuple(str, int)]: List of most common k-mers with their counts.
    """
    motifs = Counter([dna[i:i+k] for i in range(len(dna)-k+1)])
    return motifs.most_common(n)
