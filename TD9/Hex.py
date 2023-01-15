# -*- coding: utf-8 -*-
from uf import Rank_UF
import random

class Hex:
    def __init__(self, N):
        # size of the board (counting extra rows / columns)
        self.size = N+2
        # initialisation of the board (all hexagons are free)
        self.board = [[0 for j in range(self.size)] for i in range(self.size)]

        # initialisation of the Union-Find object
        nelem = self.size**2
        self.uf = Rank_UF(nelem)

        # first player to play is player 1
        self.player = 1


        l = self.size-1
        # union of sides of each player
        # player 1 is affected to the extra rows, player 2 extra columns
        for i in range(1,self.size-1):
            self.board[0][i] = 1
            self.board[l][i] = 1
            self.board[i][0] = 2
            self.board[i][l] = 2


            if i > 0:
                self.uf.union(self.hex_to_int(1,0), self.hex_to_int(i,0))
                self.uf.union(self.hex_to_int(1,l), self.hex_to_int(i,l))

                self.uf.union(self.hex_to_int(0,1), self.hex_to_int(0,i))
                self.uf.union(self.hex_to_int(l,1), self.hex_to_int(l,i))

        # get the indices in UF of the bottom and top sides of each player
        self.bot1 = self.hex_to_int(0,1)
        self.top1 = self.hex_to_int(l,1)
        self.bot2 = self.hex_to_int(1,0)
        self.top2 = self.hex_to_int(1,l)


    def hex_to_int(self, i, j):
        return i*(self.size) +j

    def print_board(self):
        for i in range(1, self.size-1):
            print(' '*(i-1),end='')
            for j in range(1, self.size-1):
                if self.board[i][j] == 0:
                    print('_', end='')
                if self.board[i][j] == 1:
                    print('X', end='')
                if self.board[i][j] == 2:
                    print('O', end='')
            print()


    def neighbours(self, i, j):
        '''
            TO IMPLEMENT
        '''
        moves = [[-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1,], [1, 0]]
        ans = []
        for dx, dy in moves:
            x, y = i + dx, j + dy
            if x >= 0 and x < self.size and y >= 0 and y < self.size and self.board[x][y] == self.player:
                ans.append([x, y])
        return ans

    def is_game_over(self):
        '''
            TO IMPLEMENT
        '''
        if self.uf.is_connected(self.bot1, self.top1) and self.player == 1:
            return True
        if self.uf.is_connected(self.bot2, self.top2) and self.player == 2:
            return True
        return False

    def random_turn(self):
        '''
            TO IMPLEMENT
        '''
        i, j = random.randint(1, self.size - 1), random.randint(1, self.size - 1)
        self.board[i][j] = self.player
        p = self.hex_to_int(i, j)
        for x, y in self.neighbours(i, j):
            q = self.hex_to_int(x, y)
            self.uf.union(p, q)
        #change player
        if self.player == 1:
                self.player = 2
        else:
            self.player = 1

    def random_play(self):
        '''
            TO IMPLEMENT
        '''
        while not self.is_game_over():
            self.random_turn()
        return self.player
        
# hex = Hex(10)
# print(hex.random_play())
# print(hex.board)