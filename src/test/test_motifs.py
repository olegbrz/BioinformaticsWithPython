import unittest
from src.main.motifs import motifs
from src.main.dna import generate_random_dna

class MotifsTestCase(unittest.TestCase):
    def test_motifs_of_empty_sequence_should_be_empty(self):
        self.assertEqual([], motifs('', 3))

    def test_number_of_results_parameter(self):
        seq = generate_random_dna(100)
        self.assertEqual(5, len(motifs(seq, 3, 5)))

    def test_motifs_count_should_be_correct(self):
        """The most common 2-mer of ACACGACTAC should be AC"""
        seq = 'ACACGACTAC'
        self.assertEqual([('AC', 4)], motifs(seq, 2, 1))



if __name__ == '__main__':
    unittest.main()
