# Bioinformatics w/ Python

Repository dedicated to the software project on Bioinformatics in Python of the course Advanced Programming in Bioinformatics.

The "Bioinformatics with Python" suite was developed to show the potential of Python solving Bioinformatics problems with a couple of lines of code.

This suite contains 7 modules with the most basic functions used in Bioinformatics.

## `dna` module

This module provides the function `generate_random_dna()` which, given a desired length, returns a random dna string.

Example:

```bash
>>> generate_random_dna(10)
'ACGACGTACG'
```

## `gc_content` module

This module computes the 'G' and 'C' nucleotides percentage in a DNA sequence with `gc_content()` function.

Example:

```bash
>>> seq = 'ACGT'
>>> gc_content(seq)
0.5
```

## `reverse_complement` module

This modules contains the `reverse_complement()` function, which, given a DNA sequence, returns its reverse complementary sequence.

Example:

```bash
>>> seq = 'GTCATCCG'
>>> revese_complement()
'CGGATGAC'
```

## `hamming_dist` module

The term 'hamming distance' is an indicator that shows the number of positions where two sequences are different, one of the implementations is as follows: initialize a counter, run through the sequences and count the times when the bases do not match.

This module provides the `hamming_dist()` function, which computes the number of positions in which two sequences differ.

Example:

```bash
>>> lhs = 'ACGT'
>>> rhs = 'TCGA'
>>> hamming_dist(lhs, rhs)
2
```

## `k_mer` module

The k-numbers are subsequences of length k within a sequence.

This module provides the `k_mer()` function, which, given a DNA sequence and a k parameter, returns all existing k-mers that contains that sequence.

Example:

```bash
>>> seq = 'ACGT'
>>> k_mer(seq, 3)
['ACG','CGT']
```

## `motifs` module

Sequence motifs are short, recurring patterns in a DNA sequence that may have a specific biological function.

This module provides the `motifs` function which, given a DNA sequence, k parameter and number of results (optional) reutrns the number of occurrences of the different k-mer in the sequence.

Example:

```bash
>>> seq = 'ACGACTAC'
>>> k = 2
>>> n_results = 4
>>> motifs(seq, k, n_results) 
[('AC', 3), ('CG', 1), ('GA', 1), ('CT', 1)]
```

## `fibonacci_rabbits` module

A very traditional problem in bioinformatics is the calculation of rabbit populations, which follow a function derived from the Fibonacci sequence. 

This module provides the `fibonacci_rabbits()` function, which, given a month, returns the number of pairs of rabbits that will exist after that time.

```bash
>>> fibonacci_rabbits(20) 
10946
```
