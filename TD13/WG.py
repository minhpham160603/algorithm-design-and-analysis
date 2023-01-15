# -*- coding: utf-8 -*-

import random
import math
from UF import *

class WG:
    def __init__(self, L): # L is the list of edges
        L.sort(key= lambda e: e[2])
        self.edges=L
        self.adj={}
        for x in L:
            if x[0] not in self.adj:
                self.adj[x[0]]={x[1]:x[2]}
            else:
                self.adj[x[0]][x[1]]=x[2]
            if x[1] not in self.adj:
                self.adj[x[1]]={x[0]:x[2]}
            else:
                self.adj[x[1]][x[0]]=x[2]

    # QUESTION 1
    def min_cycle_aux(self,w,L,S):
        # TODO
        if len(S) == 0:
            if L[0] in self.adj[L[-1]]:
                return (w + self.adj[L[0]][L[-1]], L + [L[0]])
        ans = math.inf, []
        current = L[-1]
        for v in self.adj[current]:
            if v in S:
                L.append(v)
                S.remove(v)
                tmp = self.min_cycle_aux(w + self.adj[current][v], L, S)
                if tmp[0] < ans[0]:
                    ans = tmp
                L.pop()
                S.add(v)
        return ans
            

    # QUESTION 2
    def min_cycle(self):
        # TODO
        S = set([key for key in self.adj.keys()])
        start = S.pop()
        L = [start]
        return self.min_cycle_aux(0, L, S)
 
    '''
    Question 3
    Put your answer here
    The weight W can be separated as: W = w + w', where w is the total weight on L, and w' is the total weight from L[-1] to the rest (back to L[0]).
    Now, w' = w1 + w2 + w3, where w1 is the cost from L[-1] to 1 point in the set S. w2 is the cost to visit each node at most once. w3 is the cost to go from the last node on the track back to L[0].
    Then we have w1 >= w_start, w2 >= w_S, w3 >= w_end. Then W >= w + w_start + w_S + w_end.
    '''

    # QUESTION 4
    def lower_bound(self,w,L,S): # returns low(L), with w the cost of L, and S the set of vertices not in L
        # TODO
        w_start = min(self.adj[L[0]][v] for v in S if v in self.adj[L[0]])
        w_end = min(self.adj[L[-1]][v] for v in S if v in self.adj[L[-1]])
        return w + w_start + w_end + self.weight_min_tree(S)

    # QUESTION 5
    def min_cycle_aux_using_bound(self,bestsofar,w,L,S):
        # TODO
        if len(S) == 0:
            if L[0] in self.adj[L[-1]]:
                return (w + self.adj[L[0]][L[-1]], L + [L[0]])
        if self.lower_bound(w, L, S) >= bestsofar[0]:
            return math.inf, []
        current = L[-1]
        for v in self.adj[current]:
            if v in S:
                L.append(v)
                S.remove(v)
                tmp = self.min_cycle_aux_using_bound(bestsofar, w + self.adj[current][v] , L, S)
                if tmp[0] < bestsofar[0]:
                    bestsofar = tmp
                L.pop()
                S.add(v)
        return bestsofar
        

    def min_cycle_using_bound(self):
        # TODO
        S = set([key for key in self.adj.keys()])
        start = S.pop()
        L = [start]
        return self.min_cycle_aux_using_bound((math.inf, []), 0, L, S)

#################################################################
## Auxiliary methods
#################################################################

    def weight_min_tree(self,S): # mincost among all trees whose spanned vertices are those in S
        if len(S)==1: return 0
        if len(S)==2:
            L=list(S)
            if L[0] in self.adj[L[1]]: return self.adj[L[0]][L[1]]
            else: return math.inf
        uf=UF(S)
        nr_components=len(S)
        weight=0
        for e in self.edges:
            if e[0] in S and e[1] in S:
                if uf.find(e[0])!=uf.find(e[1]):
                    weight=weight+e[2]
                    uf.union(e[0],e[1])
                    nr_components=nr_components-1
                    if nr_components==1:
                        return weight
        return math.inf

    def induce_by_subset(self,S): # reduces self.adj to keep only the edges with both ends in S
        new_adj={}
        for x in self.adj:
            for y in self.adj[x]:
                if x in S and y in S:
                    if x not in new_adj:
                        new_adj[x]={y:self.adj[x][y]}
                    else:
                        new_adj[x][y]=self.adj[x][y]
                    if y not in new_adj:
                        new_adj[y]={x:self.adj[y][x]}
                    else:
                        new_adj[y][x]=self.adj[y][x]
        self.adj=new_adj

    def display(self):
        print("Graph has "+str(len(self.adj))+" vertices")
        print()
        for x,y in self.adj.items():
            print("Neighbours of "+str(x)+":")
            for t,u in y.items():
                print(str(t)+" with weight "+str(u))
            print()
