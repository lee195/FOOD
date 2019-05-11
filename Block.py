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
    def __init__(self, prev_hash, timestamp: int):
        self.prev_hash = prev_hash
        self.timestamp = timestamp

    def __repr__(self):
        hasher = hashlib.sha256()
        hasher.update(str(self.prev_hash).encode())
        hasher.update(str(self.timestamp).encode())
        return hasher.hexdigest()


class Priority:
    def __init__(self, prio_type):
        self.prio_type = prio_type

    def __repr__(self):
        return self.prio_type


class Block:
    def __init__(self, header, data):
        self.header = header
        self.data = MerkleTree(data)
        self.hashed = self.hash_val()

    def __repr__(self):
        return str(self.header) + '\n' + str(self.data)

    def hash_val(self):
        hasher = hashlib.sha256()
        hasher.update(str(self.header).encode())
        hasher.update(str(self.data).encode())

        return hasher.hexdigest()


def generate_genesis():
    gen_header = Header("Genesis", 0)
    return Block(gen_header, ['Genesis tx'])


if __name__ == "__main__":
    genesis = generate_genesis()
    print(genesis)
    print(genesis.hashed)