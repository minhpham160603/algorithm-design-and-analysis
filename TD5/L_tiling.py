# Question 1
def middleL(n, i, j, a, b): # returns the middle of the punctured grid of type (n, i, j, a, b)
    center = i + (1 << (n - 1)) - 1, j + (1 << (n - 1)) - 1
    if a <= center[0] and b <= center[1]:
        return [(center[0] + 1, center[1]), (center[0] + 1, center[1] + 1), (center[0], center[1] + 1)]
    elif a <= center[0] and b > center[1]:
        return [(center[0] + 1, center[1]), (center[0] + 1, center[1] + 1), (center[0], center[1])]
    elif a > center[0] and b <= center[1]:
        return [(center[0], center[1]), (center[0] + 1, center[1] + 1), (center[0], center[1] + 1)]
    else:
        return [(center[0] + 1, center[1]), (center[0], center[1]), (center[0], center[1] + 1)]
# Question 2
def lower_left_hole(n, i, j, a, b): # returns the coordinates of the hole of the lower left quadrant
    center = i + (1 << (n - 1)) - 1, j + (1 << (n - 1)) - 1
    if a <= center[0] and b <= center[1]:
        return (a, b)
    return (center[0], center[1])
    

def lower_right_hole(n, i, j, a, b): # returns the coordinates of the hole of the lower right quadrant
    center = i + (1 << (n - 1)) - 1, j + (1 << (n - 1)) - 1
    if a > center[0] and b <= center[1]:
        return (a, b)
    return (center[0] + 1, center[1])

def upper_left_hole(n, i, j, a, b): # returns the coordinates of the hole of the upper left quadrant
    center = i + (1 << (n - 1)) - 1, j + (1 << (n - 1)) - 1
    if a <= center[0] and b > center[1]:
        return (a, b)
    return (center[0], center[1] + 1)

def upper_right_hole(n, i, j, a, b): # returns the coordinates of the hole of the upper right quadrant
    center = i + (1 << (n - 1)) - 1, j + (1 << (n - 1)) - 1
    if a > center[0] and b > center[1]:
        return (a, b)
    return (center[0] + 1, center[1] + 1)

# Question 3
def tile(n, i, j, a, b): # returns a list with a valid L-tiling of the punctured grid of type (n, i, j, a, b)
    if n == 1:
        return [middleL(n, i, j, a, b)]
    #low left
    ll_hole = lower_left_hole(n, i, j, a, b)
    lleft = tile(n - 1, i, j, ll_hole[0], ll_hole[1])
    #low right
    lr_hole = lower_right_hole(n, i, j, a, b)
    lright = tile(n - 1, i + (1 << (n - 1)), j, lr_hole[0], lr_hole[1])
    #upper left
    ul_hole = upper_left_hole(n, i, j, a, b)
    uleft = tile(n - 1, i, j + (1 << (n - 1)), ul_hole[0], ul_hole[1])
    #upper right
    ur_hole = upper_right_hole(n, i, j, a, b)
    uright = tile(n - 1, i + (1 << (n - 1)), j + (1 << (n - 1)), ur_hole[0], ur_hole[1])
    return lleft + lright + uleft + uright + [middleL(n, i, j, a, b)] 
    
