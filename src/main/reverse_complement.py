def reverse_complement(dna: str) -> str:
    """reverse_complement computes the reverse complement of a DNA sequence.

    Args:
        dna (str): input DNA sequence

    Returns:
        str: reverse complementary of the input sequence
    """
    complement = {'A': 'T', 'T': 'A',
                  'C': 'G', 'G': 'C'}
    return ''.join([complement[base] for base in dna[::-1]])
