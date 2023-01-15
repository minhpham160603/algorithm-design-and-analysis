from dg import *

# Question 5
def contains_pattern(s, text):
    regex = f"(.)*{s}(.)*"
    nfa = NFA(regex)
    return nfa.check_text(text)

class NFA:
    def __init__(self, s): # s is the string containing the regular expression
        self.s = s
        self.m = len(self.s)
        self.dg = DG(len(s) + 1) # the directed graph that stores the epsilon links
        self.lp = [-1 for _ in range(len(s))]
        self.rp = [-1 for _ in range(len(s))]
        self.left_right_match_or() # assigns lp and rp according to parentheses matches
        self.build_eps_links() # assigns the epsilon links in self.dg

    def __str__(self):
        n = self.m
        str_lp = 'lp: '
        str_rp = 'rp: '
        for i in range(self.m):
            if self.lp[i] == -1:
                str_lp += '-1  '
            elif self.lp[i] < 10:
                str_lp += str(self.lp[i]) + '   '
            else: str_lp += str(self.lp[i]) + '  '
            if self.rp[i] == -1:
                str_rp += '-1  '
            elif self.rp[i] < 10:
                str_rp += str(self.rp[i]) + '   '
            else: str_rp += str(self.rp[i]) + '  '
        str_lp += '\n'
        str_rp += '\n'

        str_dg = str(self.dg)

        s = '------------------\nRegular expression\n------------------\n' + 're: ' + '   '.join(self.s) + '\n'
        return s + str_lp + str_rp #+ '------------------\nCorresponding NFA\n------------------\n' + str_dg

    ## Question 1
    def left_right_match(self):
        stack = []
        for i in range(self.m):
            if self.s[i] == "(":
                stack.append(i)
            elif self.s[i] == ")":
                j = stack.pop()
                self.rp[j] = i
                self.lp[i] = j
                      

    ## Question 2
    def left_right_match_or(self):
        stack = []
        or_stack = []
        for i in range(self.m):
            if self.s[i] == "(":
                stack.append(i)
            elif self.s[i] == ")":
                j = stack.pop()
                self.rp[j] = i
                self.lp[i] = j
                if or_stack:
                    or_id = or_stack.pop()
                    self.rp[or_id] = i
                    self.lp[or_id] = j
            elif self.s[i] == "|":
                or_stack.append(i)

    ## Question 3
    def build_eps_links(self):
        for i in range(self.m):
            if self.s[i] == "(":
                self.dg.add_link(i, i + 1)
            elif self.s[i] == ")":
                self.dg.add_link(i, i + 1)
            elif self.s[i] == "*":
                self.dg.add_link(i, i + 1)
                self.dg.add_link(i, self.lp[i - 1])
                self.dg.add_link(self.lp[i - 1], i)
            elif self.s[i] == "|":
                self.dg.add_link(i, self.rp[i])
                self.dg.add_link(self.lp[i], i + 1)

    ## Question 4
    # Complexity: O(m*n)
    # Because: 2 nested for loops of len(w) compose with len self.m
    def check_text(self, w):
        K = self.dg.explore_from_subset([0])
        for i in range(len(w)):
            D = []
            for k in K:
                if k < self.m and (self.s[k] == "." or self.s[k] == w[i]):
                    D.append(k + 1)
            if len(D) == 0:
                return False
            K = self.dg.explore_from_subset(D)
        return self.m - 1 in K
                
                    
