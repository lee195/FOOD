#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 14:28:18 2019

@author: jisu
"""

import hashlib, Block, random

random.seed(0)


def min_hash(ids):
    out = []
    for i in ids:
        hasher = hashlib.sha256()
        hasher.update(i.encode('utf-8'))
        out.append(hasher.hexdigest())

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
        prio_dict[p.prio_type].append(i)

    return prio_dict

<<<<<<< HEAD
=======
def pop_prio_dict(ids, prios):
	prio_dict = read_prio_types()
	
	for i, p in zip(ids, prios):
		prio_dict[p.prio_type].append(i)
		
	return prio_dict
>>>>>>> e73bc653f1a31becd65fbd2486a810779a310370

def priority_sort(ids, prios):
    prio_dict = fill_prio_dict(ids, prios)
    block_proposal = []
    for v in prio_dict.values():
        block_proposal.append(min_hash(v))
    block_proposal.reverse()
    return [v for prio_type in block_proposal for v in prio_type]


if __name__ == "__main__":
<<<<<<< HEAD
    ids = ['1', '2', '3']
    prios = [
        Block.Priority('top'),
        Block.Priority('normal'),
        Block.Priority('top')
    ]
    print(priority_sort(ids, prios))
=======
	ids = ['1', '2', '3']
	prios = [Block.Priority('top'), Block.Priority('normal'), Block.Priority('top')]
	print(priority_sort())
	
	
	
	
>>>>>>> e73bc653f1a31becd65fbd2486a810779a310370
