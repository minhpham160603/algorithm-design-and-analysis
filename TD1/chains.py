# -*- coding: utf-8 -*-

import math
from PowerTree import *

## Q1 ##
def bin_pow(x,n):
    if n == 0:
        return 1
    elif n == 1:
        return x
    else:
        tmp = bin_pow(x, n//2)
        tmp = tmp**2
        if n%2 == 0: return tmp
        return tmp*x

## Q2 ##
def cost_bin_pow(n):
    if n <= 1:
        return 0
    if n%2 == 1:
        return cost_bin_pow(n//2) + 2
    return cost_bin_pow(n//2) + 1

## Q3 ##
def smallest_factor(n):
    max_factor = int(math.sqrt(n)) + 1
    for i in range(2, max_factor):
        if n%i == 0:
            return i
    return -1

## Q4 ##
def factor_pow(x,n):
    if n == 0:
        return 1
    elif n == 1:
        return x
    else:
        p = smallest_factor(n)
        if p == -1:
            return x*factor_pow(x, n - 1)
        else:
            q = n//p
            return factor_pow(factor_pow(x, p),q)

## Q5 ##
def cost_factor_pow(n):
    if n <= 1:
        return 0
    p = smallest_factor(n)
    if p == -1:
        return 1 + cost_factor_pow(n - 1)
    return cost_factor_pow(p) + cost_factor_pow(n // p)

def test():
    for i in range(40):
        print(f"Bin Pow n = {i}: {cost_bin_pow(i)}")
        print(f"Factor Pow: n = {i}: {cost_factor_pow(i)}")
# test()
## Q6 ##
def power_from_chain(x,chain):
    power_dict = {1: x}
    for i in range(1, len(chain)):
        power_dict[chain[i]] = power_dict[chain[i - 1]]*power_dict[chain[i] - chain[i - 1]]
    return power_dict[chain[-1]]

## Q8 ##

def power_tree_chain(n):
    tree = PowerTree()
    while n not in tree.parent:
        tree.add_layer()
    return tree.path_from_root(n)

def power_tree_pow(x,n):
    chain = power_tree_chain(n)
    return power_from_chain(x, chain)
    	   
def cost_power_tree_pow(n):
    return len(power_tree_chain(n)) - 1
  
## Q9 ##  
def compare_costs(m):
    print(f"Binary Power Cost: {cost_bin_pow(m)}")
    print(f"Factorial Power Cost: {cost_factor_pow(m)}")
    print(f"Power Tree Cost: {cost_power_tree_pow(m)}")

compare_costs(100)