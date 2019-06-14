#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 14:28:18 2019

@author: jisu
"""

import hashlib, Block, random

random.seed(0)


def min_hash(ids):
    """Performs a slightly modified Minhash correlated sampling

    Parameters:
        ids (list): List of tx ids

    Returns:
        list: A sorted list of sha256 hashvalues of ids
    """

    def hash_data(data):
        hasher = hashlib.sha256(data.encode())
        return hasher.hexdigest()

    return sorted(hash_data(i) for i in ids)


def fill_prio_dict(ids, prios):
    """Places tx ids in a dict grouped by their priority values

    Parameters:
        ids (list): List of tx ids
        prios (list): List of tx priorities

    Returns:
        dict: {tx_priority : [tx_id1, tx_id2, ...]}
    """
    prio_dict = {}
    for p_type in Block.prio_types:
        prio_dict[p_type] = []
    for i, p in zip(ids, prios):
        prio_dict[p].append(i)
    return prio_dict


def priority_sort(ids, prios):
    """Sorts tx ids by their priority

    Parameters:
        ids (list): List of tx ids
        prios (list): List of tx priorities

    Returns:
        list: The tx ids sorted by priority

    """
    prio_dict = fill_prio_dict(ids, prios)
    block_proposal = [min_hash(v) for v in prio_dict.values()]
    #change priority in list from lowest -> highest to highest -> lowest
    block_proposal.reverse()
    #return flattened list (there is one list for each priority type in the block proposal)
    return [v for prio_type in block_proposal for v in prio_type]


def consistency(block_a, block_b):
    """Calculates the similarity of two blocks

    Parameters:
        block_a, block_b (Block): the blocks to compare

    Returns:
        int: The number of tx ids unique to either of the blocks
    """
    tx_a = set(block_a.get_tx())
    tx_b = set(block_b.get_tx())
    return len(tx_a ^ tx_b)


#TODO: replace with netstats later
def netsize():
    return 9


#Using PBFT for consistency in each round
def consensus_reached(proposals):
    """PBFT consensus check on a list of block proposals
    TODO: Needs to be changed to allow similar blocks for consensus

    Parameters:
        proposals: List of block proposals

    Returns:
        True: at least 2/3 of network nodes have proposed identical blocks
        False: otherwise
    """
    # If there are not at least 2/3 network size block proposals, there cannot be a consensus
    if len(proposals) < netsize() * 2 // 3:
        return False
    for p in proposals:
        #TODO: replace count by consistency based count
        if proposals.count(p) >= netsize() * 2 // 3:
            #TODO: write consensus result to some location
            return True
    return False


if __name__ == "__main__":
    ids = ['1', '2', '3']
    prios = ['top', 'normal', 'top']
    print(priority_sort(ids, prios))
    gen = Block.generate_genesis()
    print(consistency(gen, gen))
    test_block1 = Block.Block([1], 0)
    print(consistency(gen, test_block1))
    print(consensus_reached([gen, gen, gen, gen, gen, gen]))
    print(consensus_reached([gen, gen, gen, gen, gen, test_block1]))