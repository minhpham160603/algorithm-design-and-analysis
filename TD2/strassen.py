#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np


#Q6
def mult_matrix(A,B):
    m, n = len(A), len(A[0])
    p = len(B[0])
    res = [[0]*p for _ in range(m)]
    for i in range(m):
        for j in range(p):
            for k in range(n):
                res[i][j] += A[i][k] * B[k][j]
    return res


#Q7
def cost_mult_matrix(n):
    return 2*n**3

#Functions split, merge, add_matrix and sub_matrix are given
def split(A):
    A=np.array(A)
    row, col = A.shape
    row2, col2 = row//2, col//2
    return A[:row2, :col2].tolist(), A[:row2, col2:].tolist(), A[row2:, :col2].tolist(), A[row2:, col2:].tolist()

def merge(a,b,c,d):
    return np.vstack((np.hstack((a, b)), np.hstack((c, d)))).tolist()

#Computes the matrix A+B
def add_matrix(A,B):
    n = len(A)
    C = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
                C[i][j] = A[i][j] + B[i][j]
    return C

#Computes the matrix A-B
def sub_matrix(A,B):
    n = len(A)
    C = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
                C[i][j] = A[i][j] - B[i][j]
    return C

#Q8
def strassen(A,B):
    if len(A) == 1:
        return [[A[0][0]*B[0][0]]]
    a, b, c, d = split(A)
    x, y, z, t = split(B)
    q1 = strassen(a, add_matrix(x, z))
    q2 = strassen(d, add_matrix(y, t))
    q3 = strassen(sub_matrix(d, a), sub_matrix(z, y))
    q4 = strassen(sub_matrix(b, d), add_matrix(z, t))
    q5 = strassen(sub_matrix(b, a), z)
    q6 = strassen(sub_matrix(c, a), add_matrix(x, y))
    q7 = strassen(sub_matrix(c, d), y)
    a = add_matrix(q1, q5)
    b = add_matrix(add_matrix(q2, q3), sub_matrix(q4, q5))
    c = add_matrix(add_matrix(q1, q3), sub_matrix(q6, q7))
    d = add_matrix(q2, q7)
    return merge(a, b, c, d)
    
#Q9
def cost_strassen(n):
    if n < 1:
        return 1
    return 7*cost_strassen(n-1) + 18*(2**(n-1))**2


#Q10
def convert_01(A):
    m, n = len(A), len(A[0])
    B = [[0]*n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if A[i][j] > 0:
                B[i][j] = 1
    return B

#Q11
def bin_pow(A, n):
    if n == 1:
        return A
    if n == 0:
        return [[i == j for j in range(len(A))] for i in range(len(A))]
    tmp = bin_pow(A, n//2)
    tmp = strassen(tmp, tmp)
    if n%2 == 0: 
        return convert_01(tmp)
    return convert_01(strassen(tmp, A))
    
def transitive_closure(A):
    n = len(A)
    for i in range(n):
        A[i][i] = 1
    R = bin_pow(A, n - 1)
    return R
    






