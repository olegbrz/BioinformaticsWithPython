def gc_content(dna: str) -> float:
    """gc_content computes the 'G' and 'C' nucleotides percentage in a DNA sequence.

    Args:
        dna (str): DNA string

    Returns:
        float: percentage of 'G' and 'C' (from 0 to 1).
    """
    if not len(dna):
        return 0
    else:
        return float(dna.count('G') + dna.count('C'))/len(dna)
