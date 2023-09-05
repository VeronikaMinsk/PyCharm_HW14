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

if len(combinations):
    for i, combination in enumerate(combinations, start=1):
        print(f'Вариант {i}')
        print(f'Вещи: {", ".join(combination)}')
        print(f'Общая масса: {sum(items[item] for item in combination)}')
        print('---')
else:
    print("Нет подходящих комбинаций")
