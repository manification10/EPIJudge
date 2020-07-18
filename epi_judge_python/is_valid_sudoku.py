from typing import List
import math

from test_framework import generic_test


# Check if a partially filled matrix has any conflicts.
def is_valid_sudoku(partial_assignment: List[List[int]]) -> bool:

    def hasduplicate(block):
        block = list(filter(lambda x: x!= 0, block))
        return len(block) != len(set(block))
    n = len(partial_assignment)

    if any(hasduplicate([partial_assignment[i][j] for j in range(n)])
           or hasduplicate([partial_assignment[j][i] for j in range(n)])
           for i in range(n)):
        return False

    region_size = int(math.sqrt(n))
    return all(not hasduplicate([partial_assignment[a][b] for a in range(region_size*I, region_size*(I+1))
                                 for b in range(region_size*J, region_size*(J+1))]) for I in range(region_size)
               for J in range(region_size))








if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_valid_sudoku.py',
                                       'is_valid_sudoku.tsv', is_valid_sudoku))
