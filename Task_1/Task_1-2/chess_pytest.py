import pytest
from chess import queens, generation_successful

def test_queens_invalid_arrangement():
    queens_positions = [(1, 1), (2, 3), (3, 5), (4, 7), (5, 2), (6, 4), (7, 6), (8, 7)]
    assert queens(queens_positions) == False


def test_generation_successful_length():
    successful_arrangements = generation_successful()
    assert len(successful_arrangements) == 4

def test_generation_successful_valid_arrangements():
    successful_arrangements = generation_successful()
    for queens_positions in successful_arrangements:
        assert queens(queens_positions) == True

def test_generation_successful_unique_arrangements():
    successful_arrangements = generation_successful()
    assert len(successful_arrangements) == len(set(tuple(pos) for pos in successful_arrangements))

def test_generation_successful_has_all_rows():
    successful_arrangements = generation_successful()
    for queens_positions in successful_arrangements:
        rows = [row for row, col in queens_positions]
        assert set(rows) == set(range(1, 9))
