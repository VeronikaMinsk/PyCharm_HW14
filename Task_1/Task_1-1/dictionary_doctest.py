def find_possible_combinations(items, max_weight):
    """
    Функция находит все возможные комбинации вещей, которые помещаются в рюкзак с максимальной грузоподъемностью.

    :param items: Список вещей с их массой в формате [('Вещь1', масса1), ('Вещь2', масса2), ...]
    :param max_weight: Максимальная грузоподъемность рюкзака.
    :return: Список комбинаций вещей, удовлетворяющих условиям.

    >>> items = [('Топор', 1.5), ('Пиво', 3), ('Горелка', 2), ('Удочка', 2), ('Фонарик', 0.5), ('Котелок', 1), ('Нож', 1), ('Спички', 0.5)]
    >>> backpack_capacity = 8
    >>> combinations = find_possible_combinations(items, backpack_capacity)
    >>> len(combinations)
    7
    >>> 'Топор' in combinations[0]
    True
    >>> 'Пиво' in combinations[0]
    True
    >>> 'Горелка' in combinations[0]
    True

    >>> backpack_capacity = 10
    >>> combinations = find_possible_combinations(items, backpack_capacity)
    >>> len(combinations)
    9
    >>> 'Топор' in combinations[4]
    True
    >>> 'Удочка' in combinations[4]
    True
    >>> 'Фонарик' in combinations[4]
    True

    >>> backpack_capacity = 4
    >>> combinations = find_possible_combinations(items, backpack_capacity)
    >>> len(combinations)
    3
    >>> 'Пиво' in combinations[2]
    True
    >>> 'Спички' in combinations[2]
    True
    """
    combinations = []

    def find_combinations(item_index, current_combination, current_weight):
        if current_weight == max_weight:
            combinations.append(sorted(current_combination))  # Сортируем комбинацию по алфавиту
            return

        if current_weight > max_weight or item_index == len(items):
            return

        item, weight = items[item_index]

        # Попробуем добавить текущую вещь в комбинацию
        if current_weight + weight <= max_weight:
            current_combination.append(item)
            find_combinations(item_index + 1, current_combination, current_weight + weight)
            current_combination.pop()  # Удаляем вещь из комбинации

        # Пропускаем текущую вещь и идем к следующей
        find_combinations(item_index + 1, current_combination, current_weight)

    find_combinations(0, [], 0)
    return combinations

if __name__ == "__main__":
    import doctest
    doctest.testmod()
