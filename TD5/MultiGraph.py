import math
import random
## Question 5 ##
def random_element(dict):
    # TO COMPLETE
    sumv = sum(dict.values())
    prob = [v/sumv for v in dict.values()]
    key = [k for k in dict.keys()]
    return random.choices(key, prob)[0]

## Question 7 ##
def random_cut(m):
    # TO COMPLETE
    partition = { x: [] for x in m.adj.keys()}
    while (len(m.adj) > 2):
        i, j = m.random_edge()
        partition[i].append(j)
        if j in partition:
            partition[i] += partition[j]
            del partition[j]
        m.contract(i, j)
    x = [k for k in partition.keys()]
    c = m.adj[x[0]][x[1]]
    return (c, [x[0]] + partition[x[0]])
    
    
def mincut_karger(L, p): # p is the desired error bound
    # TO COMPLETE
    n = L[0]
    k = math.ceil(math.log(p)/math.log(1 - 2/(n*(n - 1))))
    m = MultiGraph(L)
    res = random_cut(m)
    for i in range(k - 1):
        mincut = random_cut(m)
        if mincut[0] < res[0]:
            res = mincut
    return str(res)


## Contains Questions 4 and 6 ##
class MultiGraph:
    def __init__(self, L):
        self.adj = {}
        self.deg = {}
        for x in L[1]:
            if x[0] not in self.adj:
                self.adj[x[0]] = {x[1]: x[2]}
                self.deg[x[0]] = x[2]
            else:
                self.adj[x[0]][x[1]] = x[2]
                self.deg[x[0]] += x[2]
            if x[1] not in self.adj:
                self.adj[x[1]] = {x[0]: x[2]}
                self.deg[x[1]] = x[2]
            else:
                self.adj[x[1]][x[0]] = x[2]
                self.deg[x[1]] += x[2]

    def subset_from_integer(self, i):# i is an integer between 1 and 2^n - 2, with n the number of vertices
        subset = {}
        for x in self.adj:
            if i % 2 == 1:
                subset[x] = True
            i = i >> 1
        return subset

    def cutsize(self, i):# i is an integer between 1 and 2^n - 2, with n the number of vertices
        subset = self.subset_from_integer(i)
        res = 0
        for x, y in self.adj.items():
            for t, u in y.items():
                if x in subset and not t in subset:
                    res += u
        return [res, [x for x in subset]] 

    def display(self):
        for x, y in self.adj.items():
            print("Neighbors of " + str(x) + ", which has degree " + str(self.deg[x]))	
            for t, u in y.items(): 
                print(str(t) + " with multiplicity " + str(u))
    
    ## Question 4 ##
    def contract(self, i, j):# contracts edge i, j (i absorbs j)
        # TO COMPLETE
        self.deg[i] -= self.adj[i][j]
        del self.adj[i][j]
        del self.adj[j][i]
        #direct all edges connect to j to i
        for k, v in self.adj[j].items():
            del self.adj[k][j]
            self.adj[k][i] = self.adj[k].get(i, 0)
            self.adj[k][i] += v
            self.deg[i] += v
            self.adj[i][k] = self.adj[k][i]
        del self.adj[j]
        del self.deg[j]

    ## Question 6.1 ##
    def random_vertex(self):
        # TO COMPLETE
        return random_element(self.deg)

    ## Question 6.2 ##
    def random_edge(self):
        # TO COMPLETE
        i = self.random_vertex()
        j = random_element(self.adj[i])
        return (i, j)
