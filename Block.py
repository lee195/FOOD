
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 22:44:41 2019

@author: jisu
"""

import hashlib, random


prio_types = ['normal', 'urgent', 'emergency', 'top']
random.seed(0)


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
	def __init__(self, header, prio, data):
		self.header = header
		self.prio = prio
		self.data = data
		self.hashed = self.hash_val()
		
	def __repr__(self):
		return str(self.header.timestamp)
	
	def hash_val(self):
		hasher = hashlib.sha256()
		hasher.update(str(self.header).encode())
		hasher.update(str(self.prio).encode())
		hasher.update(str(self.data).encode())
				
		return hasher.hexdigest()
	
	
def generateGenesis():
	gen_header = Header("Genesis", 0)
	gen_prio = Priority('top')
	return Block(gen_header, gen_prio, [])


if __name__ == "__main__":
	genesis = generateGenesis()
	print(genesis)
	print(genesis.header)
	print(genesis.hashed)
	print(genesis.prio)

