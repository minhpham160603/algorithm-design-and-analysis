# -*- coding: utf-8 -*-

from uf import Rank_UF

import random


def draw_grid(grid, N):
    for ii in range(N):
        i = ii+1
        for j in range(N):
            if grid[i][j] == 0:
                print('X', end='')
            else:
                print(' ', end='')
        print()

def pos_to_int(N, i, j):
    return N*i+j


def get_vacant_neighbors(G,N,i,j):
    '''
        TO IMPLEMENT
    '''
    moves = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    ans = []
    for dx, dy in moves:
        x, y =  i + dx, j + dy
        if x >= 0 and x < len(G) and y >= 0 and y < N and G[x][y]:
            ans.append([x, y])
    return ans
            

def make_vacant(UF, G, N, i, j):
    '''
        TO IMPLEMENT
    '''
    G[i][j] = True
    n = pos_to_int(N, i, j)
    vacant_neighbors = get_vacant_neighbors(G, N, i, j)
    for x, y in vacant_neighbors:
        m = pos_to_int(N, x, y)
        UF.union(n, m)
     

def ratio_to_percolate(N):
    '''
        TO IMPLEMENT
    '''
    UF = Rank_UF((N + 2)*N)
    G = [[False]*N for _ in range(N + 2)]
    G[0] = [True]*N
    G[-1] = [True]*N
    p1 = pos_to_int(N, 0, 0)
    p2 = pos_to_int(N, N + 1, 0)
    count = 0
    for j in range(1, N):
        q1 = pos_to_int(N, 0, j)
        q2 = pos_to_int(N, N + 1, j)
        UF.union(p1, q1)
        UF.union(p2, q2)
    while not UF.is_connected(p1, p2):
        i, j = random.randint(1, N), random.randint(0, N - 1)
        if not G[i][j]:
            make_vacant(UF, G, N, i, j)
            count += 1
    return count/(N*N)