#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 16:02:59 2019

@author: jisu
"""
import hashlib, Block, random


random.seed(0)


class m_node:
	def __init__(self, left: Block.Block, right: Block.Block):
		hasher = hashlib.sha256()
		hasher.update(left.hash_val + right.hash_val)
		self.val = hasher.hexdigest()
		self.left = left
		self.right = right


class merkle_tree:
	def __init__(self, data: list[Block.Block]):
		