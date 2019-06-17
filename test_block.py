import unittest
import Block
import random


class TestBlock(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        random.seed(0)

    # def test_genesis(self):
    #     expected_hash = '810043e3e9dbfe3616a8b038f2886379bc9a04585c968f1ff9d291497766e980'
    #     expected_tx = ['Genesis tx']
    #     gen = Block.generate_genesis()
    #     self.assertEqual(expected_hash, gen.hashed)
    #     self.assertEqual(expected_tx, gen.get_tx())

    def test_merkle(self):
        expected_root = '88cd668c2056e926cf9f6dad3acbeebf0c1e093da5ab7aceb244e65661d7e35e'

        merkle_tree = Block.MerkleTree([1, 2, 3, 4])
        self.assertEqual(expected_root, merkle_tree.root)
        for tx in [1, 2, 3, 4]:
            self.assertTrue(merkle_tree.verify(tx))


if __name__ == "__main__":
    unittest.main()