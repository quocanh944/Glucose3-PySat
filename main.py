from itertools import product, combinations
from pysat.solvers import Glucose3
from colorama import Back
import os

def load_from_file(filename):
    res = []
    if os.path.exists(filename):
        with open(filename) as g:
            m, n = [int(it) for it in g.readline().split()]
            for line in g:
                res.append([int(it) if it != '.' else -1 for it in line.strip().split()])

    return m, n, res

def bioconditional(p,q):
    return p == q

def ands(data_set):
    return not(False in data_set)

def get_adjacent_cells(i, j, m, n):
    # Returns a list of adjacent cell coordinates for cell (i,j)
    return [(x*n + y) + 1 for x, y in product(range(i-1, i+2), range(j-1, j+2))
            if 0 <= x < m and 0 <= y < n]

def generate_p_bicondition_q(adjacent_cells, cell_number):
    p = list(combinations(adjacent_cells, cell_number))
    q = []
    for k in p:
        q.append([-1 * x for x in list(filter(lambda x: x not in k, adjacent_cells))])
    return p, q

def print_result(model, matrix):
    m = len(matrix)
    n = len(matrix[0])

    for i in range(m):
        for j in range(n):
            if matrix[i][j] != -1:
                if ((i*n + j) + 1) in model:
                    print(Back.GREEN + str(matrix[i][j]), end=' ')
                else:
                    print(Back.RED + str(matrix[i][j]), end=' ')
            else:
                if ((i*n + j) + 1) in model:
                    print(Back.GREEN + ' ', end=' ')
                else:
                    print(Back.RED + ' ', end=' ')
        print()

def main():
    m, n, matrix = load_from_file('./input.txt')

    g = Glucose3()

    # Glucose syntax
    # [
    #     [1,-2,3], # clause
    #     [4,-5,6], # and
    # ]

    for i in range(m):
        for j in range(n):
            cell_number = matrix[i][j]
            if cell_number >= 0:
                adjacent_cells = get_adjacent_cells(i, j , m, n)
                truth_table = list(product([True,False],repeat = len(adjacent_cells)))
                p, q = generate_p_bicondition_q(adjacent_cells, cell_number)
                for index in range(len(p)):
                    for row in truth_table:
                        truth_p = list(row[:cell_number])
                        truth_q = list(row[cell_number:])

                        if bioconditional(ands(truth_p), ands([(not x) for x in truth_q])) == False:
                            all_literals = list(p[index]) + [-1 * x for x in q[index]]
                            clause = [lit if row[pos] == False else -1 * lit for pos, lit in enumerate(all_literals)]
                            g.add_clause(clause)

    if g.solve():
        print_result(g.get_model(), matrix)
    else:
        print("Can't solve.")


if (__name__ == "__main__"):
    main()
