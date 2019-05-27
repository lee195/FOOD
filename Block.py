#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 22:44:41 2019

@author: jisu
"""

import hashlib, random

prio_types = ['normal', 'urgent', 'emergency', 'top']
random.seed(0)


class MerkleTree:
    def __init__(self, data):
        def hash_data(data_a, data_b):
            hasher = hashlib.sha256()
            hasher.update(str(data_a).encode() + str(data_b).encode())
            return hasher.hexdigest()

        self.data = [data.copy()]
        layer = data.copy()
        while len(layer) > 1:
            if len(layer) % 2 != 0:
                layer.append(0)
            #replace layer by the pair-wise hash of elements in layer
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


class Header:
    def __init__(self, prev_hash, merkle_root):
        self.prev_hash = prev_hash
        self.merkle_root = merkle_root

    def __repr__(self):
        hasher = hashlib.sha256()
        hasher.update(str(self.prev_hash).encode())
        hasher.update(str(self.merkle_root).encode())
        return hasher.hexdigest()


class Block:
    def __init__(self, data, prev_hash):
        self.data = MerkleTree(data)
        self.header = Header(prev_hash, self.data.root)
        self.hashed = self.hash_val()

    def __repr__(self):
        return str(self.header) + '\n' + str(self.data)

    def hash_val(self):
        hasher = hashlib.sha256()
        hasher.update(str(self.header).encode())
        hasher.update(str(self.data.root).encode())

        return hasher.hexdigest()

    def get_tx(self):
        return self.data.data[0]


#TODO: move to different module
def generate_genesis():
    return Block(["Genesis tx"], 0)


if __name__ == "__main__":
    genesis = generate_genesis()
    print(genesis)
    print(genesis.hashed)
    print(100 * '-')
    print(MerkleTree([1, 2, 3, 4]))
    print(genesis.get_tx())