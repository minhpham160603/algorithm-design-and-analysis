# -*- coding: utf-8 -*-


import math
# from test import test7

def binary_search_rec(A,v,left,right):
    if (right >= left):
        mid = left + (right - left)//2 # using `(right + left)//2` can lead to an integer overflow
        if (v == A[mid]):
            return mid
        elif (v < A[mid]):
            return binary_search_rec(A,v,left,mid-1)
        else:
            return binary_search_rec(A,v,mid+1,right)
    
    return -1
        
## Q1 ##
def binary_search(A,v):
    l, r = 0, len(A) - 1
    while l <= r:
        mid = (l + r)//2
        if A[mid] == v:
            return mid
        elif A[mid] < v:
            l = mid + 1
        else:
            r = mid - 1
    return -1

def cost_binary_search(n):
    if n == 0: return 1
    if n == 1: return 3
    return cost_binary_search(math.ceil(n/2)) + 3
    
## Q2 ##
def ternary_search(A,v):
    start, end = 0, len(A) - 1
    while start <= end:
        n1 = start + (end - start)//3
        n2 = end - (end - start)//3
        if v == A[n1]: return n1
        elif v == A[n2]: 
            return n2
        elif v < A[n1]:
            end = n1 - 1
        elif v > A[n1] and v < A[n2]:
            start = n1 + 1
            end = n2 - 1
        elif v > A[n2]:
            start = n2 + 1
    return -1
            
        

def cost_ternary_search(n):
    if n == 0:
        return 1
    elif n == 1:
        return 5
    return cost_ternary_search(math.ceil(n/3)) + 5
    
    
def cost_binary_search_real(A,v):
    if len(A) == 0: return 0

    left = 0
    right = len(A) - 1
    cost =  0
    while (right >= left):
        mid = left + (right - left)//2
        if (v == A[mid]):
            return cost + 1
        elif (v < A[mid]):
            right = mid - 1
            cost += 2
        else:
            left = mid + 1
            cost += 2

    return cost

def cost_ternary_search_real(A,v):
    start, end = 0, len(A) - 1
    cost = 0
    while start <= end:
        n1 = start + (end - start)//3
        n2 = end - (end - start)//3
        if v == A[n1]: return cost + 1
        elif v == A[n2]: 
            return cost + 2
        elif v < A[n1]:
            end = n1 - 1
            cost += 3
        elif v > A[n1] and v < A[n2]:
            start = n1 + 1
            end = n2 - 1
            cost += 5
        else:
            start = n2 + 1
            cost += 5
    return cost
        

## Q3 ##
def exponential_search(A,v):
    r = 1
    while r < len(A) - 1 and A[r] < v:
        r = min(len(A) - 1, r*2)
    l = r//2
    while l <= r:
        mid = (l + r)//2
        if A[mid] == v:
            return mid
        elif A[mid] < v:
            l = mid + 1
        else:
            r = mid - 1
    return -1
    
        

def cost_exponential_search(v):
    k = math.ceil(math.log2(v))
    return k + cost_binary_search(2**(k - 1))

## Q4 ##
def interpolation_search(A,v):
    l, r = 0, len(A) - 1
    if r == l or A[r] == A[l]:
        return l if A[l] == v else -1
    while l <= r:
        k = l + int((v - A[l])*(r - l)/(A[r] - A[l]))
        #print(l, k, r)
        if k > r:
            return -1
        elif k < l:
            return -1
        if A[k] == v:
            return k
        elif A[k] < v:
            l = k + 1
        else:
            r = k - 1
    return -1

## Q6 ##
def findFirstOccurrence(A, v):
    l, r = 0, len(A) - 1
    while l <= r:
        mid = (l + r)//2
        if A[mid] == v:
            if mid > 0 and A[mid - 1] == v:
                r = mid - 1
            else:
                return mid
        elif A[mid] < v:
            l = mid + 1
        else:
            r = mid - 1
    return -1

def findLastOccurrence(A, v):
    l, r = 0, len(A) - 1
    while l <= r:
        mid = (l + r)//2
        if A[mid] == v:
            if mid < len(A) - 1 and A[mid + 1] == v:
                l = mid + 1
            else:
                return mid
        elif A[mid] < v:
            l = mid + 1
        else:
            r = mid - 1
    return -1

## Q7 ##
def binary_search_update(A,v):
    l, r = 0, len(A) - 1
    while l <= r:
        mid = (l + r)//2
        if A[mid] == v:
            return mid
        elif A[mid] < v:
            l = mid + 1
        else:
            r = mid - 1
    return l

def findKClosestElements(A, v, k):
    i = binary_search_update(A, v)
    # print(i)
    l, r = i - 1, i
    res = [], []
    while r - l < k + 1:
        # print(l, r)
        if l < 0:
            res[1].append(A[r])
            r += 1
        elif r > len(A) - 1:
            res[0].append(A[l])
            l -= 1
        elif abs(A[l] - v) < abs(A[r] - v):
            res[0].append(A[l])
            l -= 1
        else:
            res[1].append(A[r])
            r += 1  
    res[0].reverse()
    return res[0] + res[1]

## Q8 ##
def findFrequency(A):
    current = 0
    data = {}
    while current < len(A):
        end = findLastOccurrence(A, A[current])
        data[A[current]] = end - current + 1
        current = end + 1
    return data
