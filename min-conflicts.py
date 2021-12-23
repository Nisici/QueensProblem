import queens_problem as qs
import random as rd
def min_conflicts(csp, max_steps):
    current = csp.initialValues
    k = 0
    for i in range(max_steps):
        if csp.isGoalState(current):
            print('SOLUTION FOUND IN ', i, 'STEPS')
            return current
        var = k
        value = conflicts(csp, var, current)
        current[var] = value
        k+=1
        if k >= len(current):
            k = 0

    return False

# returns the value to be assigned to variable var so that there are minimum conflicts possible
# in the problem at state current. This function first counts the number of constraints violated
# by a variable and then returns value that minimizes the constraints violations.
def conflicts(csp,var,current):
    # target queen row
    conflicts = csp.getConflicts(current,var)
    min_val = min(conflicts)
    min_val_indices = [i for i, j in enumerate(conflicts) if j == min_val]
    i = rd.randint(0,len(min_val_indices)-1)
    return min_val_indices[i]

if __name__ == '__main__':
    steps = 100000
    Q = qs.csp_queens(500)
    print("INITIAL STATE : ")
    Q.printGrid(Q.initialValues)
    ris_state = min_conflicts(Q,steps)
    print("FINAL STATE : ")
    if ris_state:
        Q.printGrid(ris_state)
    else:
        print("SOLUTION NOT FOUND IN ", steps, " STEPS")