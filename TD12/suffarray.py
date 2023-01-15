# -*- coding: utf-8 -*-

def str_compare(a, b):
    N = min(len(a),len(b))
    for i in range(N):
        if a[i] < b[i]:
            return -1
        elif a[i] > b[i]:
            return 1

    return len(a)-len(b)

def str_compare_m(a,b, m):
    if len(a) >= m and len(b) >= m:
        # len(a) >= m and len(b) >= m
        return str_compare(a[:m], b[:m])
    else:
        # len(a) < m or len(b) > m
        return str_compare(a,b)

def longest_common_prefix(a, b):
    N = min(len(a),len(b))
    for i in range(N):
        if a[i] != b[i]:
            return i
    return N


class suffix_array:
    # Question 1
    def __init__(self, t):
        self.T = t
        self.N = len(t)
        self.suffId = [i for i in range(self.N)]

        # TODO: order suffId by lexicographic order
        # SORT
        suffix = [self.T[i:] for i in range(self.N)]
        self.suffId.sort(key = lambda i: suffix[i])

    def suffix(self, i):
        return self.T[self.suffId[i]:]

    # Question 2
    def findL(self, S):
        # TO IMPLEMENT
        l, r = -1, self.N 
        while l + 1 < r:
            m = (l + r)//2
            if str_compare_m(S, self.suffix(m), len(S)) <= 0:
                r = m
            else:
                l = m
        return r

    # Question 2
    def findR(self,S):
        # TO IMPLEMENT
        l, r = -1, self.N 
        while l + 1 < r:
            m = (l + r)//2
            if str_compare_m(S, self.suffix(m), len(S)) >= 0:
                l = m
            else:
                r = m
        return r

    def findLR(self,S):
        return (self.findL(S),self.findR(S))

# Question 3
# The complexity of findL is O(mlog(N)) since
# we divide the input by two each time we search 
# for the correct position (binary search) costing O(log(N))
# and in each operation,the complexity is O(m) 
# since str_compare_m cost O(m)


# Question 4
def KWIC(sa, S, c = 15):
    # TO IMPLEMENT
    l, r = sa.findLR(S)
    suffix = [sa.suffId[i] for i in range(l, r)]
    ans = []
    for idx in suffix:
        start = max(0, idx - c)
        end = min(idx + len(S) + c, sa.N)
        ans.append(sa.T[start:end])
    return ans

# Question 5
def longest_repeated_substring(sa):
    # TO IMPLEMENT
    ans = ""
    for i in range(sa.N - 1):
        l = longest_common_prefix(sa.suffix(i), sa.suffix(i + 1))
        if l > len(ans):
            ans = sa.suffix(i)[:l]
    return ans

#Going further
def longest_repeated_substring_ktimes(sa, k):
    ans = ""
    for i in range(sa.N - k + 1):
        l = longest_common_prefix(sa.suffix(i), sa.suffix(i + k - 1))
        if l > len(ans):
            ans = sa.suffix(i)[:l]
    return ans
    
