#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 16:02:59 2019

@author: jisu
"""
import hashlib, Block, random

random.seed(0)


class merkle_tree:
    def __init__(self, data):
        def hash_data(data_a, data_b):
            hasher = hashlib.sha256()
            hasher.update(
                str(data_a).encode('utf-8') + str(data_b).encode('utf-8'))
            return hasher.hexdigest()

        self.data = [data.copy()]
        layer = data.copy()
        while len(layer) > 1:
            if len(layer) % 2 != 0:
                layer.append(0)
            layer = [
                hash_data(layer[i], layer[i + 1])
                for i in range(0, len(layer), 2)
            ]
            self.data.append(layer)
        self.root = layer[0]

    def __repr__(self):
        out = ""
        for layer in self.data[::-1]:
            out += str(layer) + "\n"
        return out[:-1]


if __name__ == "__main__":
    test_tree = merkle_tree([1, 2, 3, 4, 5])
    print(test_tree)
    print(test_tree.root)