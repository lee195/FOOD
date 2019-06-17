import unittest
import Consensus, Block
import random


class TestBlock(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        random.seed(0)

    def setUp(self):
        self.ids = ['1', '2', '3']
        self.prios = ['top', 'normal', 'top']
        self.test_block1 = Block.Block([1, 2, 3], 0)
        self.test_block2 = Block.Block([4, 5, 6], 0)

    def test_priosort(self):
        expected = [
            '4e07408562bedb8b60ce05c1decfe3ad16b72230967de01f640b7e4729b49fce',
            '6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b',
            'd4735e3a265e16eee03f59718b9b5d03019c07d8b6c51f90da3a666eec13ab35'
        ]
        actual = Consensus.priority_sort(self.ids, self.prios)

        self.assertEqual(expected, actual)

    def test_consistency(self):
        self.assertEqual(
            Consensus.consistency(self.test_block1, self.test_block1), 0)

        self.assertEqual(
            Consensus.consistency(self.test_block1, self.test_block2), 6)

    def test_consensus(self):
        test = [
            self.test_block1, self.test_block1, self.test_block1,
            self.test_block1, self.test_block1, self.test_block1
        ]
        self.assertTrue(Consensus.consensus_reached(test))
        test = [
            self.test_block1, self.test_block1, self.test_block1,
            self.test_block1, self.test_block1
        ]
        self.assertFalse(Consensus.consensus_reached(test))
        test = [
            self.test_block2, self.test_block1, self.test_block1,
            self.test_block1, self.test_block1
        ]
        self.assertFalse(Consensus.consensus_reached(test))


if __name__ == "__main__":
    unittest.main()