import unittest
from src.main.reverse_complement import reverse_complement


class ReverseComplementTestCase(unittest.TestCase):
    def test_reverse_complement_of_empty_sequence_should_be_empty_sequence(self):
        self.assertEqual('', reverse_complement(''))

    def test_reverse_complement_of_ACGT_should_be_ACGT(self):
        self.assertEqual('ACGT', reverse_complement('ACGT'))


if __name__ == '__main__':
    unittest.main()
