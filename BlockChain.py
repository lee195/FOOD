#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 16:02:59 2019

@author: jisu
"""
import hashlib, Block, random

random.seed(0)


class CappedHash:
    """Hash container of fixed capacity"""

    def __init__(self, data, capacity):
        """Inits self.data as the last n elements of data where n is capacity.
        """
        self.cap = capacity
        if len(data) > capacity:
            self.data = dict(enumerate(data[-capacity:]))
        else:
            self.data = dict(enumerate(data))
        self.ptr = len(data) % capacity

    def __repr__(self):
        return self.data.__str__()

    def add_entry(self, entry):
        """Adds entry to the container. The oldest entry is replaced at full cap."""
        self.data[self.ptr % self.cap] = entry
        self.ptr += 1

    def get_nth_last_entry(self, index):
        return self.data[(self.ptr - index) % self.cap]


def generate_genesis():
    return Block.Block(['Genesis tx'], 0)


memory = CappedHash([generate_genesis()], 10)

if __name__ == "__main__":
    print('Blockchain Simulation: Distributed Object Ordering with Fairness\n')
    print(memory)