# -*- coding: utf-8 -*-
from suffarray import *


def algo_check(T, res, out):
    #print('Text:', T)
    if res == out:
        return True
        pass
    else:
        print('Failure. Expected ', res, ' but obtained ', out)
        return False

def test1():
    successful = True

    print('checking suffix array construction...')
    T = 'banana'
    sa = suffix_array(T)
    res = [5, 3, 1, 0, 4, 2]
    successful &= algo_check(T, res, sa.suffId)

    T = 'abracadabra'
    sa = suffix_array(T)
    res = [10, 7, 0, 3, 5, 8, 1, 4, 6, 9, 2]
    successful &= algo_check(T, res, sa.suffId)

    T = 'to be, or not to be'
    sa = suffix_array(T)
    res = [16, 2, 9, 6, 13, 5, 17, 3, 18, 4, 10, 15, 1, 7, 11, 8, 12, 14, 0]
    successful &= algo_check(T, res, sa.suffId)

    if successful:
        print('  Success!')


def find_check(sa, key, dir, expected):
    #print('Text:',T)
    #print('query', key)
    res = sa.findL(key) if dir == 'L' else sa.findR(key)
    if res == expected:
        return True
        #print('find{} success ! L={}'.format(dir, res))
        pass
    else:
        print('find{} failure. Expected {} but got {}'.format(dir, expected, res))
        print('text: {}, key: {}'.format(sa.T, key))
        return False

def test2():
    successful = True

    T = 'banana'
    sa = suffix_array(T)
    T2 = 'abracadabra'
    sa2 = suffix_array(T2)

    if sa.findL('b') is not None:
        print('checking findL...')
        successful &= find_check(sa, 'b', 'L', 3)
        successful &= find_check(sa, 'bl', 'L', 4)
        successful &= find_check(sa2, 'bra', 'L', 5)
        successful &= find_check(sa2, 'can', 'L', 8)
        for this_sa in [sa, sa2]:
            successful &= find_check(this_sa, '', 'L', 0)
            for i in range(0,this_sa.N-1):
                successful &= find_check(this_sa, this_sa.suffix(i), 'L', i)
            successful &= find_check(this_sa, this_sa.suffix(this_sa.N-1) + 'X', 'L', this_sa.N)
        if successful:
            print('  Success!')
    else:
        print('skipping findL (unimplemented)')

    successful = True
    if sa.findR('b') is not None:
        print('checking findR...')
        successful &= find_check(sa, 'b', 'R', 4)
        successful &= find_check(sa, 'bl', 'R', 4)
        successful &= find_check(sa2, 'bra', 'R', 7)
        successful &= find_check(sa2, 'can', 'R', 8)
        for this_sa in [sa, sa2]:
            successful &= find_check(this_sa, '', 'R', this_sa.N)
            for i in range(0,this_sa.N-1):
                # compute R starting from i
                S = this_sa.suffix(i)
                res = i
                while res < this_sa.N and str_compare_m(this_sa.suffix(res), S, len(S)) <= 0:
                    res += 1
                successful &= find_check(this_sa, S, 'R', res)
            successful &= find_check(this_sa, this_sa.suffix(this_sa.N-1) + 'X', 'R', this_sa.N)
        if successful:
            print('  Success!')
    else:
        print('skipping findR (unimplemented)')

def check_kwic(sa, key, c, matches):
    res = KWIC(sa, key, c)
    if sorted(res) != sorted(matches):
        print('Failure. Expected:')
        for x in sorted(matches):
            print(x)
        print('But got:')
        for x in sorted(res):
            print(x)
        print('key: {}, context: {}'.format(key, c))
        print('text: {}'.format(sa.T))
        return False
    return True

def test4():
    successful = True

    T = 'abracadabra'
    sa = suffix_array(T)
    if KWIC(sa, "cad", 3) is None:
        print("skipping KWIC (unimplemeneted)")
        return
    print('checking KWIC...')
    successful &= check_kwic(sa, "cad", 3, ['bracadabr'])
    successful &= check_kwic(sa, "bra", 3, ['abracad', 'adabra'])

    T = "In computer science, a suffix array is a sorted array of all suffixes of a string. It is a data structure used, among others, in full text indices, data compression algorithms and within the field of bibliometrics. \
Suffix arrays were introduced by Manber & Myers (1990) as a simple, space efficient alternative to suffix trees. They had independently been discovered by Gaston Gonnet in 1987 under the name PAT array (Gonnet, Baeza-Yates & Snider 1992).\
Li, Li & Huo (2016) gave the first in-place O ( n ) {\displaystyle {\mathcal {O}}(n)} {\mathcal {O}}(n) time suffix array construction algorithm that is optimal both in time and space, where in-place means that the algorithm only needs O ( 1 ) {\displaystyle {\mathcal {O}}(1)} {\mathcal {O}}(1) additional space beyond the input string and the output suffix array.\
Enhanced suffix arrays (ESAs) are suffix arrays with additional tables that reproduce the full functionality of suffix trees preserving the same time and memory complexity.[1] The suffix array for a subset of all suffixes of a string is called sparse suffix array.[2] Multiple probabilistic algorithms have been developed to minimize the additional memory usage including an optimal time and memory algorithm."
    sa = suffix_array(T)
    matches = [\
               'ter science, a suffix array is a sor',
               'd array of all suffixes of a string.',
               'alternative to suffix trees. They ha',
               'l {O}}(n) time suffix array construc',
               'and the output suffix array.Enhanced',
               'array.Enhanced suffix arrays (ESAs) ',
               'ays (ESAs) are suffix arrays with ad',
               'nctionality of suffix trees preservi',
               'lexity.[1] The suffix array for a su',
               ' subset of all suffixes of a string ',
               ' called sparse suffix array.[2] Mult']
    successful &= check_kwic(sa, "suffix", 15, matches)
    matches = [\
               'ence, a suffix array is a sorted ar',
               'ay is a sorted array of all suffixe',
               'etrics. Suffix arrays were introduc',
               'r the name PAT array (Gonnet, Baeza',
               'n) time suffix array construction a',
               ' output suffix array.Enhanced suffi',
               'nhanced suffix arrays (ESAs) are su',
               'As) are suffix arrays with addition',
               '[1] The suffix array for a subset o',
               ' sparse suffix array.[2] Multiple p']
    successful &= check_kwic(sa, "array", 15, matches)
    matches = [\
               'ta compression algorithms and within th',
               'y construction algorithm that is optima',
               'means that the algorithm only needs O (',
               ' probabilistic algorithms have been dev',
               'ime and memory algorithm.']
    successful &= check_kwic(sa, "algorithm", 15, matches)
    if successful:
        print('  Success!')

def test5():
    successful = True

    if longest_repeated_substring(suffix_array('blabla')) is None:
        print('skipping longest_repeated_substring (unimplemented)')
        return
    print('checking longest_repeated_substring...' )
    T = 'banana'
    sa = suffix_array(T)
    S = longest_repeated_substring(sa)
    successful &= algo_check(T, 'ana', S)

    T = 'abracadabra'
    sa = suffix_array(T)
    S = longest_repeated_substring(sa)
    successful &= algo_check(T, 'abra', S)

    T = 'to be, or not to be'
    sa = suffix_array(T)
    S = longest_repeated_substring(sa)
    successful &= algo_check(T, 'to be', S)

    T = "In computer science, a suffix array is a sorted array of all suffixes of a string. It is a data structure used, among others, in full text indices, data compression algorithms and within the field of bibliometrics. \
Suffix arrays were introduced by Manber & Myers (1990) as a simple, space efficient alternative to suffix trees. They had independently been discovered by Gaston Gonnet in 1987 under the name PAT array (Gonnet, Baeza-Yates & Snider 1992).\
Li, Li & Huo (2016) gave the first in-place O ( n ) {\displaystyle {\mathcal {O}}(n)} {\mathcal {O}}(n) time suffix array construction algorithm that is optimal both in time and space, where in-place means that the algorithm only needs O ( 1 ) {\displaystyle {\mathcal {O}}(1)} {\mathcal {O}}(1) additional space beyond the input string and the output suffix array.\
Enhanced suffix arrays (ESAs) are suffix arrays with additional tables that reproduce the full functionality of suffix trees preserving the same time and memory complexity.[1] The suffix array for a subset of all suffixes of a string is called sparse suffix array.[2] Multiple probabilistic algorithms have been developed to minimize the additional memory usage including an optimal time and memory algorithm."
    sa = suffix_array(T)
    S = longest_repeated_substring(sa)
    res = ' ) {\displaystyle {\mathcal {O}}('
    successful = successful and algo_check(T, res, S)

    if successful:
        print('  Success!')

test1()
test2()
test4()
test5()
