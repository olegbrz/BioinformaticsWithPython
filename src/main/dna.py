import random


def generate_random_dna(length: int) -> str:
    """generate_random_dna generates a random DNA string given a length.

    Args:
    	length (int): desired dna length.

    Returns:
		str: DNA string. E.g.: 'AGCTCACTGACTT' for length = 13
	"""

    dna = ''.join([random.choice('ACGT') for _ in range(length)])
    return dna
