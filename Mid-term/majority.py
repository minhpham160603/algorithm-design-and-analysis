from math import log, log2
from random import randint, choice

## Question 1
# Return frequency of v in L[start:stop].
# The worst-case run time is: O(n)
# Because: We loop through all element between start and stop, which is bounded by len n.
def getFrequency(v, L, start, stop):
    count = 0
    for i in range(start, stop):
        if L[i] == v:
            count += 1
    return count


## Question 2
# Return majority element of L if it exists, otherwise 'False'.
# The worst-case run time is: O(n^2)
# Because: We loop through elements in L, and each time we call getFrequency which cost O(n),
# hence the complexity is O(n^2).
def getMajorityNaively(L):
    n = len(L)
    for i in L:
        m = getFrequency(i, L, 0, n)
        if m > n//2:
            return i
    return False


## Question 3
# Return majority element of L if it exists, otherwise 'False'.
# The worst-case run time is: O(nlog(n))
# Because: C(n) = 2*C(n//2) + 2*O(n). Using master theorem, we deduce C(n) = O(nlog(n))
def getMajorityDaC(L):
    def helpGetMajorityDaC(start, stop):
        if start + 1 == stop:
            return L[start]
        n = stop - start
        mid = (start + stop)//2
        a = helpGetMajorityDaC(start, mid)
        b = helpGetMajorityDaC(mid, stop)
        x = getFrequency(a, L, start, stop) if a else 0
        y = getFrequency(b, L, start, stop) if b else 0
        if x >= y and x > n//2:
            return a
        elif y > n//2:
            return b
        else:
            return False
    return helpGetMajorityDaC(0, len(L))


## Question 4
# Return majority element of M if it exists, otherwise 'False'.
# The worst-case run time is: O(nlog(n))
# Because: C(n) = 4*C(n//4) + 4n. Using master theorem, we deduce C(n) = O(nlog(n))
def getMajorityInMatrixDaC(M):
    def helpGetMajorityDaC(rowStart, rowStop, colStart, colStop):
        if rowStart + 1 == rowStop:
            return M[rowStart][colStart]
        n = rowStop - rowStart
        
        rowMid, colMid = (rowStart + n//2), (colStart + n//2)
        a = helpGetMajorityDaC(rowStart, rowMid, colStart, colMid)
        b = helpGetMajorityDaC(rowStart, rowMid, colMid, colStop)
        c = helpGetMajorityDaC(rowMid, rowStop, colMid, colStop)
        d = helpGetMajorityDaC(rowMid, rowStop, colStart, colMid)
        data = {}
        data[a] = getFrequencyFromMatrix(a, M, rowStart, rowStop, colStart, colStop) if a else 0
        data[b] = getFrequencyFromMatrix(b, M, rowStart, rowStop, colStart, colStop) if b else 0
        data[c] = getFrequencyFromMatrix(c, M, rowStart, rowStop, colStart, colStop) if c else 0
        data[d] = getFrequencyFromMatrix(d, M, rowStart, rowStop, colStart, colStop) if d else 0
        maxfreq = [0, 0]
        for k, v in data.items():
            if v > maxfreq[1]:
                maxfreq = [k, v]
        if maxfreq[1] > n**2//2:
            return maxfreq[0]
        return False
    return helpGetMajorityDaC(0, len(M), 0, len(M[0]))    
    

# Returns the frequency of v in M[rowStart:rowStop][colStart:colStop].
def getFrequencyFromMatrix(v, M, rowStart, rowStop, colStart, colStop):
    freq = 0
    for row in range(rowStart, rowStop):
        freq += getFrequency(v, M[row], colStart, colStop)
    return freq


## Question 5
# Return majority element of L if it exists, otherwise 'False'.
# The worst-case run time is: O(n)
# Because: We only loop through all element of the list, each time with operation O(1), there is no nested loop, count also cost O(n), hence the complexity is O(n).
def getMajorityBoyerMoore(L):
    freq = 0
    curr = None
    for i in L:
        if freq == 0:
            freq += 1
            curr = i
        elif i != curr:
            freq -= 1
    n = L.count(curr)
    if n > len(L)//2:
        return curr
    return False


## Question 6
# Return majority element of L with probability at least p if it exists, otherwise 'False'.
# Probability for one try finding the existing majority element is at least: 1/2. Because the number of occurences of the majority element is strictly greater than 1/2.
# Probability that m tries all fail (assuming a majority element exists) is at most: 1/2^m. Because each independent time the probability to fail is at most 1/2.
def getMajorityRandomized(L, p):
    m = int(log2(1/(1 - p)))
    for _ in range(m):
        i = choice(L)
        f = getFrequency(i, L, 0, len(L))
        if f > len(L)//2:
            return i
    return False
        