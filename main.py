# test solving n queens problem using min conflicts algorithm
# steps: maximum number of steps before exiting
# it can print the initial and final grid, useful only if n is small.
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
