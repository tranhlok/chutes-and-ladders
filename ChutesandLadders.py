import numpy as np
import copy
import time

# The dictionary of chutes and ladder. 
chutes_ladders = {1: 38, 4: 14, 16: 6, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100, 98: 78, 95: 75, 93: 73, 87: 24, 64: 60, 62: 19, 56: 53, 49: 11, 48: 26}
cd_list = list(chutes_ladders.keys())
# Vector to solve for our result later
b = np.ones(101)
b[100] = 0
# Dictionary of dices: key is a face of that dice and value is its corresponding probability
black = {4:2/3, 0:1/3}
red = {6:1/3, 2:2/3}
green = {5:1/2, 1:1/2}
blue = {3:1}

def row_calculator(board, square_no, dice):
    faces = list(dice.keys())
    # blue dice only has one face on it, so I design a specific part for it
    #since we flip the side of the equation, most of them are subtracted 
    #from the original value that specific point in the matrix
    if dice == blue:
        f1 = faces[0]
        p1 = dice[f1]
        if square_no + 3 < 100:
            if square_no + f1 in cd_list:
                board[square_no][chutes_ladders[square_no + f1]] -= p1
            else:
                board[square_no][square_no + f1] -= p1
        else:
            board[square_no][100] = -1
    # for other dices
    else:
        #get the dice value
        f1 = faces[0]
        f2 = faces[1]
        p1 = dice[f1]
        p2 = dice[f2]
        #algorithm
        if square_no + f1 < 100:
            if square_no+ f1 in cd_list:
                board[square_no][chutes_ladders[square_no+f1]] -= p1
            else:
                board[square_no][square_no+f1] -= p1
            if square_no+f2 in cd_list:
                board[square_no][chutes_ladders[square_no+f2]] -= p2
            else:
                board[square_no][square_no+f2] -= p2
        elif square_no + f2 < 100:
            board[square_no][100] = -p1
            if square_no + f2 in cd_list:
                board[square_no][chutes_ladders[square_no + f2]] -= p2
            else:
                board[square_no][square_no + f2] -= p2
        else:
            board[square_no][100] = -1

def update(board, square_no, dice):
    #initialize the value of the square to be 1
    board[square_no][square_no] = 1
    if square_no == 100:
        return
    #run the calculation based on the picked dice. 0 denotes black, 1 denotes red, 2 denotes green, and 3 denotes blue
    if dice == 0:
        row_calculator(board, square_no, black)
    if dice == 1:
        row_calculator(board, square_no, red)
    if dice == 2:
        row_calculator(board, square_no, green)
    if dice == 3:
        row_calculator(board, square_no, blue)

def number_of_moves(board, policy):
    #update the board
    for i in range(101):
        update(board, i, policy[i])
    try:
        x = np.linalg.solve(board, b)
        return x
    # since we can not use blue dice on square 53 (which leads to infinite loop), the matrix lines from 53 
    #created by blue dice contain all 0.
    # which leads to singular matrix and can not be solved. Return a valid value when an error is reached.
    except np.linalg.LinAlgError as err:
        if 'Singular matrix' in str(err):
            return [float('inf')]

def update_policy(policy, x):
    #check if the new policy makes the x value smaller
    #compute bottom up
    for i in range(99, -1, -1):
        for j in range(4):
            new_board = np.zeros((101, 101))
            policy_new = copy.deepcopy(policy)
            policy_new[i] = j
            x_matrix = number_of_moves(new_board, policy_new)
            x2 = x_matrix[0]
            #if new policy improve optimal moves, get new policy and optimal moves
            if x2 < x:
                policy[i] = j
                x = x2
    return policy, x

def main():
    start = time.time()
    #use the green dice as the first set of policy, tests showing that initialize a all green dice policy results in best value
    policy = [2 for i in range(101)]
    moves = float('inf')
    #number of trials
    trials = 1
    policy_old = copy.deepcopy(policy)
    policy, moves = update_policy(policy, moves)
    while policy_old != policy:
        policy_old = copy.deepcopy(policy)
        policy, moves = update_policy(policy, moves)
        trials += 1
    end = time.time()
    time_run = end - start
    print("Optimal Average Number of Moves Expected to Complete the Game: ",moves)
    print(f"Execution time of the program is {time_run} seconds with {trials} trials.")
    print("Final Policy, with 0 denotes black, 1 denotes red, 2 denotes green, and 3 denotes blue \n", policy)
    return 0

main()