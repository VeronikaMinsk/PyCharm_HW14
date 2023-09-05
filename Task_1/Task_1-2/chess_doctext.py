import itertools
import random
import doctest

def queens(queens_positions):
    for i in range(len(queens_positions)):
        for j in range(i + 1, len(queens_positions)):
            row1, col1 = queens_positions[i]
            row2, col2 = queens_positions[j]
            if row1 == row2 or col1 == col2 or abs(row1 - row2) == abs(col1 - col2):
                return False
    return True

def generation_successful():
    successful_args = []
    permutations = list(itertools.permutations(range(1, 9)))
    random.shuffle(permutations)
    for permutation in permutations:
        queens_positions = [(i + 1, permutation[i]) for i in range(8)]
        if queens(queens_positions):
            successful_args.append(queens_positions)
            if len(successful_args) == 4:
                break
    return successful_args

def test_queens_function():
    """

    >>> queens([(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 1)])
    False
    >>> queens([(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 2)])
    False
    >>> queens([(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 3)])
    False
    >>> queens([(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 4)])
    False
    """
    pass


def test_generation_successful_function():
    """
    >>> successful_arrangements = generation_successful()
    >>> len(successful_arrangements)
    4
    >>> all(isinstance(arrangement, list) and len(arrangement) == 8 for arrangement in successful_arrangements)
    True
    >>> all(queens(arrangement) for arrangement in successful_arrangements)
    True
    """
    pass

if __name__ == "__main__":
    doctest.testmod()
