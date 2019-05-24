#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 14:28:18 2019

@author: jisu
"""

import hashlib, Block, random

random.seed(0)


def min_hash(ids):
    def hash_data(data):
        hasher = hashlib.sha256(data.encode())
        return hasher.hexdigest()

    out = [hash_data(i) for i in ids]

    out.sort()
    return out


def read_prio_types():
    prio_dict = {}
    for p_type in Block.prio_types:
        prio_dict[p_type] = []
    return prio_dict


def fill_prio_dict(ids, prios):
    prio_dict = read_prio_types()
    for i, p in zip(ids, prios):
        prio_dict[p].append(i)

    return prio_dict


def priority_sort(ids, prios):
    prio_dict = fill_prio_dict(ids, prios)
    block_proposal = [min_hash(v) for v in prio_dict.values()]
    #change priority in list from lowest -> highest to highest -> lowest
    block_proposal.reverse()
    #return flattened list (there is one list for each priority type in the block proposal)
    return [v for prio_type in block_proposal for v in prio_type]


def consistency(block_a, block_b):
    tx_a = block_a.get_tx()
    tx_b = block_b.get_tx()
    return sum([1 for t in tx_a if not t in tx_b] +
               [1 for t in tx_b if not t in tx_a])


if __name__ == "__main__":
    ids = ['1', '2', '3']
    prios = ['top', 'normal', 'top']
    print(priority_sort(ids, prios))
    gen = Block.generate_genesis()
    print(consistency(gen, gen))