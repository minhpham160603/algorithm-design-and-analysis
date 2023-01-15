import random
import math
from UF import *

nr_calls=0

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

    def min_cycle_aux(self,w,L,S):
        global nr_calls
        nr_calls=nr_calls+1
        a=L[0]; b=L[-1]
        if len(S)==0:
            if a not in self.adj[b]:
                return (math.inf,[])
            else:
                Lc=L[:]
                Lc.append(a)
                return (w+self.adj[b][a],Lc)
        res=(math.inf,[])
        for x in self.adj[b]:
            if x in S:
                L.append(x); S.remove(x)
                outx=self.min_cycle_aux(w+self.adj[b][x],L,S)
                L.pop(); S.add(x)
                if outx[0]<res[0]:
                    res=outx
        return res

    def min_cycle(self):
        global nr_calls
        nr_calls=0
        S=self.vertex_set()
        a=S.pop()
        res = self.min_cycle_aux(0,[a],S)
        print("number of calls to min_cycle_aux: "+str(nr_calls))
        return res

    def vertex_set(self): # returns the set with all vertices of the graph
        S=set()
        for x in self.adj:
            S.add(x)
        return S

    def lower_bound(self,w,L,S):
        # returns low(L), with w the cost of L, and S the set of vertices not in L
        a=L[0]
        b=L[-1]
        min_a=math.inf
        min_b=math.inf
        for x in self.adj[a]:
            if x in S and self.adj[a][x]<min_a:
                min_a=self.adj[a][x]
        for x in self.adj[b]:
            if x in S and self.adj[b][x]<min_b:
                min_b=self.adj[b][x]
        return w+min_a+min_b+self.weight_min_tree(S)

    def min_cycle_aux_using_bound(self,bestsofar,w,L,S):
        global nr_calls
        nr_calls=nr_calls+1
        a=L[0]; b=L[-1]
        if len(S)==0:
            if a not in self.adj[b] or w+self.adj[b][a]>=bestsofar:
                return (math.inf,[])
            else:
                Lc=L[:]
                Lc.append(a)
                return (w+self.adj[b][a],Lc)

        if self.lower_bound(w,L,S)>=bestsofar:
            return (math.inf,[])

        res=(math.inf,[])
        for x in self.adj[b]:
            if x in S:
                L.append(x); S.remove(x)
                outx=self.min_cycle_aux_using_bound(bestsofar,w+self.adj[b][x],L,S)
                L.pop(); S.add(x)
                if outx[0]<res[0]:
                    res=outx
                if outx[0]<bestsofar:
                    bestsofar=outx[0]
        return res

    def min_cycle_using_bound(self):
        global nr_calls
        nr_calls=0
        S=self.vertex_set()
        a=S.pop()
        res = self.min_cycle_aux_using_bound(math.inf,0,[a],S)
        print("number of calls to min_cycle_aux_using_bound: "+str(nr_calls))
        return res

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



##############################
## Approximation algorithms ##
##############################

### Provided

    def random_cycle(self):
        # construct a random cycle
        T = [x for x in self.adj]
        random.shuffle(T)
        return (T, self.eval_cycle(T))

    def eval_cycle(self, T):
        # evaluate a cycle
        w = 0
        for i in range(1,len(self.adj)):
            w += self.adj[T[i - 1]][T[i]]

        w += self.adj[T[len(self.adj) - 1]][T[0]]
        return w

    def get(self, T, i):
        # returns the node at L[i] (cyclic: Safe if i < 0 or i > len(L))
        return T[i % len(self.adj)]

#########################
## Greedy construction ##
#########################

    ## Question 1
    def greedily_select_edges(self):
        C = set()
        nodes = [n for n in self.adj.keys()]
        uf = UF(nodes)
        degree = {n: 0 for n in nodes}
        for e in self.edges:
            if degree[e[0]] <= 1 and degree[e[1]] <= 1:
                if uf.is_connected(e[0], e[1]):
                    if len(C) < len(nodes) - 1:
                        continue
                    C.add(tuple(e))
                    return C
                else:
                    uf.union(e[0], e[1])
                    degree[e[0]] += 1
                    degree[e[1]] += 1
                    C.add(tuple(e))
                    
    ## Question 2
    def build_cycle_from_edges(self, edges):
        start_edge = next(iter(edges))
        edges.remove(start_edge)
        T = [start_edge[1]]
        W = start_edge[2]
        while len(edges):
            for e in edges:
                if T[-1] in e:
                    edges.remove(e)
                    W += e[2]
                    if e[0] == T[-1]:
                        T.append(e[1])
                    else:
                        T.append(e[0])
                    break
        return (W, T)
                    

    ## Greedy approximation algorithm
    def greedy_min(self):
        selected_edges = self.greedily_select_edges()
        return self.build_cycle_from_edges(selected_edges)

###########
## 2-opt ##
###########

    ## Question 3
    def evaluate_flip(self, T, i, j):
        v1, v2 = self.get(T, i - 1), self.get(T, i)
        u2, u3 = self.get(T, j), self.get(T, j + 1)
        
        if u2 in self.adj[v1] and u3 in self.adj[v2]:
            return self.adj[v1][v2] + self.adj[u2][u3] \
                - self.adj[v1][u2] - self.adj[v2][u3]
        return -math.inf
        

    ## Question 4
    def find_best_opt2(self, T):
        ans = (None, 0)
        for i in range(len(T)):
            for j in range(i + 1, len(T)):
                g = self.evaluate_flip(T, i, j)
                if g > ans[1]:
                    ans = ((i, j), g)
        return ans
    ## Question 5
    def opt_2(self, W, T):
        flip = self.find_best_opt2(T)
        if not flip[0]:
            return (W, T)
        (i, j), g = flip
        self.flip(T, i, j)
        return (W - g, T)

    ## Perform a flip in the list of nodes
    def flip(self, T, i, j):
        k = j + 1
        T[i:k] = reversed(T[i:k])

    ## Question 6
    def neighborhood_search_opt2(self, W, T):
        W_new, T_new = self.opt_2(W, T)
        while W_new != W:
            W = W_new
            W_new, T_new = self.opt_2(W_new, T_new)
        return (W_new, T_new)
