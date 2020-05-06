import pdb
from copy import deepcopy
from helpers import normalize, blur

def initialize_beliefs(grid):
    height = len(grid)
    width = len(grid[0])
    area = height * width
    belief_per_cell = 1.0 / area
    beliefs = deepcopy(grid)
    for i in range(len(beliefs)):
        for j in range(len(beliefs[0])):
            beliefs[i][j] = belief_per_cell
    return beliefs

def sense(color, grid, beliefs, p_hit, p_miss):
    #
    # TODO - implement this in part 2
    #
    new_beliefs = deepcopy(beliefs)
    # loop through all grid cells
    for i in range(len(beliefs)):
        for j in range(len(beliefs[0])):
            # check if the sensor reading is equal to the color of the grid cell
            # if so, hit = 1
            # if not, hit = 0
            hit = (color == grid[i][j])
            new_beliefs[i][j] = beliefs[i][j] * (hit * p_hit + (1-hit) * p_miss)
            #new_beliefs.append(beliefs[i][j] * (hit * p_hit + (1-hit) * p_miss))

    # sum up all the components
    s=0.0
    for i in range(len(new_beliefs)):
        for j in range(len(new_beliefs[0])):
            s = s + new_beliefs[i][j]  
    
    # divide all elements of q by the sum to normalize
    for i in range(len(new_beliefs)):
        for j in range(len(new_beliefs[0])):
            new_beliefs[i][j] = new_beliefs[i][j] / s
   
    return new_beliefs

def move(dy, dx, beliefs, blurring):
    height = len(beliefs)
    width = len(beliefs[0])
    new_G = [[0.0 for i in range(width)] for j in range(height)]
    for i, row in enumerate(beliefs):
        for j, cell in enumerate(row):
            new_i = (j + dx ) % height
            new_j = (i + dy ) % width
            #pdb.set_trace()
            new_G[int(new_i)][int(new_j)] = cell
    return blur(new_G, blurring)