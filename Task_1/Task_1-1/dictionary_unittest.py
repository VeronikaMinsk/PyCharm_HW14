import unittest

def find_possible_combinations(items, max_weight):
    combinations = []

    def find_combinations(item_index, current_combination, current_weight):
        if current_weight == max_weight:
            combinations.append(current_combination)
            return

        if current_weight > max_weight or item_index == len(items):
            return

        item, weight = items[item_index]
        if current_weight + weight <= max_weight:
            find_combinations(item_index + 1, current_combination + [item], current_weight + weight)

        find_combinations(item_index + 1, current_combination, current_weight)

    find_combinations(0, [], 0)
    return combinations

class TestFindPossibleCombinations(unittest.TestCase):
    def test_valid_combination(self):
        backpack_capacity = 8
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
        items_list = [(item, weight) for item, weight in items.items()]
        combinations = find_possible_combinations(items_list, backpack_capacity)
        self.assertTrue(len(combinations) > 0)

    def test_invalid_combination(self):
        backpack_capacity = 1
        items = {
            'Топор': 1.5,
            'Пиво': 3,
        }
        items_list = [(item, weight) for item, weight in items.items()]
        combinations = find_possible_combinations(items_list, backpack_capacity)
        self.assertEqual(len(combinations), 0)

    def test_empty_items(self):
        backpack_capacity = 5
        items = {}
        items_list = [(item, weight) for item, weight in items.items()]
        combinations = find_possible_combinations(items_list, backpack_capacity)
        self.assertEqual(len(combinations), 0)

if __name__ == '__main__':
    unittest.main()
