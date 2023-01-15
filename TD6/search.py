# -*- coding: utf-8 -*-

### For comparing strings

def string_compare(P,S):
    for j in range(len(P)):
        if not P[j] == S[j]:
            return False
    return True
    
    
### naive string matcher    
def string_match(T, P):
    n = len(T)
    m = len(P)
    res = []
    for i in range(n):
        if(string_compare(T[i:i + m], P) and len(T[i:i+m]) == len(P)):
            res.append(i)
    return res
### number of characters
base = 256

### karp_rabin_sum 

def hash_string_sum(S):
    return sum([ord(c) for c in S])

def hash_string_sum_update(h, Ti, Tim):
    return h - ord(Ti) + ord(Tim)
    
def karp_rabin_sum(T,P):
    m = len(P)
    res = []
    h  = hash_string_sum(T[0:m])
    hP = hash_string_sum(P)
    hit = 0
    for i in range(len(T) - m + 1):
        if h == hP:
            if T[i: i + m] == P:
                res.append(i)
            else:
                hit += 1
        if (i + m >= len(T)): break
        h  = hash_string_sum_update(h, T[i], T[i + m])
    return res, hit
        
    
### karp_rabin_mod
    
def hash_string_mod(S, q):
    res = ord(S[0])%q
    d = 256%q
    for i in range(len(S) - 1):
        res = ((res)*(d) + (ord(S[i + 1])%q))%q
    return res
        
    
def hash_string_mod_update(h, q, Ti, Tim, dm):
    return (256*(h - dm*ord(Ti)) + ord(Tim))%q
    
def karp_rabin_mod(T,P,q):
    d = 256
    dm = 1
    m = len(P)
    for i in range(m - 1):
        dm *= d%q

    res = []
    h  = hash_string_mod(T[0:m], q)
    hP = hash_string_mod(P, q)
    hit = 0
    for i in range(len(T) - m + 1):
        if h == hP:
            if T[i: i + m] == P:
                res.append(i)
            else:
                hit += 1
        if (i + m >= len(T)): break
        h  = hash_string_mod_update(h, q, T[i], T[i + m], dm)
    return res, hit

