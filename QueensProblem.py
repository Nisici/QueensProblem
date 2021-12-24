import numpy as np
import random as rd
"""""
An instance of this class represents the queen's problem, you can initialize it with a certain size
which will create a grid nxn with n queens randomly placed.
"""""


class csp_queens:
    # n: size of the grid nxn and number of queens to be placed randomly
    # grid(i,j) = 0 if there isn't a queen in that position, grid(i,j)=1 otherwise
    # state: a set of variables, each variable represents a queen in a certain columns,
    #        the domain of the variables is [0, size-1], an assignment to a variable means that
    #        the queen on that column is located in a certain row
    #        i.e.: Q_1 = 5 => Queen located in column 1 is in row 5.
    def __init__(self, n):
        self.size = n
        self.initialValues = []
        self.grid = np.zeros((n,n), dtype = int)
        for col in range(n):
            row = rd.randint(0, n - 1)
            self.initialValues.append(row)
            self.grid[row, col] = 1

    #returns a random chosen variable, a variable corresponds to a column of the grid where a queen is located.
    def getConflictVariable(self):
        return rd.randint(0,self.size-1)
    # returns all the conflicts in this state for the variable var
    def getConflicts(self,state,var):
        conflicts = [0] * len(state)
        for col in range(len(state)):
            if col != var:
                # other queen row
                otherVal = state[col]
                # same row
                conflicts[otherVal] += 1
                # same diagonal
                for row in range(len(state)):
                    if row != otherVal:
                        if (abs(otherVal - row) == abs(col - var)):
                            conflicts[row] += 1
        return conflicts
    # print grid where 0 means no queens are placed in that position and 1 the opposite
    def printGrid(self, state):
        self.grid = np.zeros((self.size, self.size), dtype=int)
        for col in range(self.size):
            self.grid[state[col], col] = 1
        print(self.grid)
    # returns true if state is goal state, false otherwise
    def isGoalState(self, state):
        for col1 in range(len(state)):
            for col2 in range(len(state)):
                if col1 != col2:
                    # there are 2 queens in the same row
                    if state[col1] == state[col2]:
                        return False
                    # there are 2 queens in the same diagonal
                    if abs(col1 - col2) == abs(state[col1] - state[col2]):
                        return False
        return True

