import pytest
from dictionary import find_possible_combinations

def test_find_possible_combinations_with_valid_combinations():
    items = [
        ('Топор', 1.5),
        ('Пиво', 3),
        ('Горелка', 2),
        ('Удочка', 2),
        ('Фонарик', 0.5),
        ('Котелок', 1),
        ('Нож', 1),
        ('Спички', 0.5)
    ]
    backpack_capacity = 8
    combinations = find_possible_combinations(items, backpack_capacity)
    assert len(combinations) > 0

def test_find_possible_combinations_with_no_valid_combinations():
    items = [
        ('Топор', 10),
        ('Пиво', 20),
        ('Горелка', 15)
    ]
    backpack_capacity = 5
    combinations = find_possible_combinations(items, backpack_capacity)
    assert len(combinations) == 0

def test_find_possible_combinations_with_zero_capacity():
    items = [
        ('Топор', 1.5),
        ('Пиво', 3),
        ('Горелка', 2)
    ]
    backpack_capacity = 0
    combinations = find_possible_combinations(items, backpack_capacity)
    assert len(combinations[0]) == 0

def test_find_possible_combinations_with_single_item_exceeding_capacity():
    items = [
        ('Топор', 10),
        ('Пиво', 3),
        ('Горелка', 2)
    ]
    backpack_capacity = 5
    combinations = find_possible_combinations(items, backpack_capacity)
    assert len(combinations[0]) == 2


if __name__ == '__main__':
    pytest.main()


@pytest.fixture
def items_list():
    items = {
        'Топор': 1.5,
        'Пиво': 3,
        'Горелка': 2,
        'Удочка': 2,
        'Фонарик': 0.5,
        'Котелок': 1,
        'Нож': 1,
        'Спички': 0.5
    }
    return [(item, weight) for item, weight in items.items()]

def test_valid_combinations(items_list):
    backpack_capacity = 8.0
    combinations = find_possible_combinations(items_list, backpack_capacity)
    assert len(combinations) > 0

def test_combination_weight(items_list):
    items = {
        'Топор': 1.5,
        'Пиво': 3,
        'Горелка': 2,
        'Удочка': 2,
        'Фонарик': 0.5,
        'Котелок' : 1,
        'Нож' : 1,
        'Спички' : 0.5
    }
    backpack_capacity = 8.0
    combinations = find_possible_combinations(items_list, backpack_capacity)
    for combination in combinations:
        total_weight = sum(items[item] for item in combination)

def test_no_combinations(items_list):
    items = {
        'Топор': 1.5,
        'Пиво': 3,
        'Горелка': 2,
        'Удочка': 2,
        'Фонарик': 0.5,
        'Котелок' : 1,
        'Нож' : 1,
        'Спички' : 0.5
    }
    backpack_capacity = 1.0
    combinations = find_possible_combinations(items_list, backpack_capacity)
    assert len(combinations) == 3
