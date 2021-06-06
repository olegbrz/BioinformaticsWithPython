import unittest
from src.main.dna import generate_random_dna


class DNA_TestCase(unittest.TestCase):
    def test_dna_length_should_be_as_requested(self):
        self.assertEqual(3, len(generate_random_dna(3)))

    def test_dna_should_only_contain_ACGT(self):
        valid_chars = ['A', 'C', 'G', 'T']
        random_dna = generate_random_dna(10)
        matched_list = [nucleotide in valid_chars for nucleotide in random_dna]
        self.assertTrue(all(matched_list))

if __name__ == '__main__':
    unittest.main()
