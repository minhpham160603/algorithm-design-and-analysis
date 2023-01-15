from random import randint, uniform

## Question 7
# Return a bit string of length n uniformly at random from {0, 1}^n.
def createBitStringUniformly(n):
    l = []
    for i in range(n):
        l.append(randint(0, 1))
    return l
        


## Question 8
# Return a new bit string that performed single-bit flip mutation on a copy of x.
def singleBitFlip(x):
    x_new = x.copy()
    i = randint(0, len(x) - 1)
    x_new[i] = 1 - x_new[i]
    return x_new


## Question 9
# Return a new bit string that performed standard bit mutation on a copy of x.
# Expected number of different bits between x and the mutant: 1. It is the expectation of random variable of binomial coefficient with param: 1/n.
def standardBitMutation(x):
    x_new = x.copy()
    for i in range(len(x)):
        p = uniform(0, 1)
        if p <= 1/len(x):
            x_new[i] = 1 - x_new[i]
    return x_new
    


## Question 10
# Return a tuple (x, it), where x is the best solution found and it is the number of iterations.
def rsh(n, f, terminated, mutation):
    x = createBitStringUniformly(n)
    it = 0
    while not terminated(x, it):
        y = mutation(x)
        if f(y) >= f(x):
            x = y
        it += 1
    return x, it
        


## Question 11
# (1 + 1) EA on OneMax (on n bits)
#    Pr[A_i] ≥ ((1 - 1/n)^i)/n ≥ ((1 - 1/n)^(n - 1))/n
#    Expected run time is at most: n^2/(1 - 1/n)^(n - 1) = n^2 as n tends to infinity.
#
# RLS on LeadingOnes (on n bits)
#    Pr[A_i] = 1/n
#    Expected run time is at most: n^2.