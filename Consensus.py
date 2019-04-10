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
		hasher.update(i)
		out.append(hasher.hexdigest())
	return out.sort()
	

def read_prio_types():
	prio_dict = {}
	for p_type in Block.prio_types:
		prio_dict[p_type] = []
	return prio_dict


def pop_prio_dict(ids, prios):
	prio_dict = read_prio_types()
	
	for i, p in zip(ids, prios):
		prio_dict[p.prio_type].append(i)
		
	return prio_dict


def priority_sort(ids, prios: list[Block.Priority]):
	prio_dict = pop_prio_dict(ids, prios)
	block_proposal = []
	for k, v in prio_dict:
		v = min_hash(v)
		block_proposal.append(v)
	return block_proposal

if __name__ == "__main__":
	ids = ['1', '2', '3']
	prios = [Block.Priority('top'), Block.Priority('normal'), Block.Priority('top')]
	print(priority_sort())
	
	
	
	
