#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 16:02:59 2019

@author: jisu
"""
import hashlib, Block, random

random.seed(0)

memory = []

#TODO: decide consistency model

#TODO: replace with netstats at some point

if __name__ == "__main__":
    print('Blockchain Simulation: Distributed Object Ordering with Fairness\n')
    memory.append(Block.generate_genesis())
    for entry in memory:
        print(str(entry) + '\n')