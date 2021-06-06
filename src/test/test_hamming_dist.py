import unittest
from src.main.hamming_dist import hamming_dist

class HammingDistanceTestCase(unittest.TestCase):
    def test_hamming_distance_of_two_empty_sequences_should_be_0(self):
        self.assertEqual(0, hamming_dist('',''))

    def test_hamming_distance_of_totally_different_sequences_should_be_their_length(self):
        lhs = 'ACGT'
        rhs = 'TGCA'
        self.assertEqual(len(lhs), hamming_dist(lhs, rhs))

    def test_hamming_distance_of_sequences_that_differ_in_two_nucleotides_should_be_2(self):
        lhs = 'ACGTACGT'
        rhs = 'AAATACGT'
        self.assertEqual(2, hamming_dist(lhs, rhs))

    def test_hamming_distance_of_the_same_sequence_should_be_0(self):
        lhs = 'ACGTACGT'
        self.assertEqual(0, hamming_dist(lhs, lhs))

if __name__ == '__main__':
    unittest.main()
