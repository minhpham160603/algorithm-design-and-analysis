# -*- coding: utf-8 -*-

# Q1
import math

def poly_mult(P,Q):
    m = len(P) #degree
    n = len(Q) #degree
    res = [0]*(m + n - 1)
    for i in range(m):
        for j in range(n):
            res[i + j] += P[i]*Q[j]
    return res 

def cost_poly_mult(n): 
    return 2*n**2 - 2*n + 1

# Q2

def poly_add(P,Q):
    m, n = len(P), len(Q)
    res = [0]*max(m, n)
    for i in range(max(m, n)):
        if i < m:
            res[i] += P[i]
        if i < n:
            res[i] += Q[i]
    return res
         
def neg(P):
    return [i*(-1) for i in P]
   
def shift(P,k):
   return [0]*k + P
  
# Q3  
  
def poly_kara_mult(P,Q):
    n = len(P)
    if n == 1:
        return [P[0]*Q[0]]
    k = math.ceil(n//2)
    h0 = poly_kara_mult(P[:k], Q[:k])
    h2 = poly_kara_mult(P[k:], Q[k:])
    h1 = poly_kara_mult(poly_add(P[:k], P[k:]), poly_add(Q[:k], Q[k:]))
    tmp = shift(poly_add(h1, neg(poly_add(h0, h2))), k)
    res = poly_add(h0, tmp)
    res = poly_add(res, shift(h2, 2*k))
    return res 

def cost_poly_kara_mult(n):
    if n == 1:
        return 1
    return 3*cost_poly_kara_mult(math.ceil(n/2)) + 4*n

# Q4 

def cost_poly_tc3_mult(n):
    if n == 1: return 1
    if n == 2: return 3
    return 5*cost_poly_tc3_mult(math.ceil(n/3)) + 30*n

# Q5 hybrid
   
def poly_switch_mult(d,P,Q):
    n = len(P)
    if n <= d:
        return poly_mult(P, Q)
    else:
        k = math.ceil(n//2)
        h0 = poly_switch_mult(d, P[:k], Q[:k])
        h2 = poly_switch_mult(d, P[k:], Q[k:])
        h1 = poly_switch_mult(d, poly_add(P[:k], P[k:]), poly_add(Q[:k], Q[k:]))
        tmp = shift(poly_add(h1, neg(poly_add(h0, h2))), k)
        res = poly_add(h0, tmp)
        res = poly_add(res, shift(h2, 2*k))
        return res

def cost_switch_mult(d,n):
    if n <= d:
        return 2*n**2 - 2*n + 1
    return 3*cost_switch_mult(d, math.ceil(n/2)) + 4*n

   
