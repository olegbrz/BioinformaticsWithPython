import unittest
from src.main.gc_content import gc_content


class GC_ContentTestCase(unittest.TestCase):
    def test_gc_content_of_ACGT_should_be_50(self):
        self.assertEqual(0.5, gc_content('ACGT'))

    def test_gc_content_of_empty_sequence_should_be_0(self):
        self.assertEqual(0, gc_content(''))

    def test_gc_content_of_AAAA_should_be_0(self):
        self.assertEqual(0, gc_content('AAAA'))

    def test_gc_content_of_GCGC_should_be_100(self):
        self.assertEqual(1, gc_content('GCGC'))


if __name__ == '__main__':
    unittest.main()
