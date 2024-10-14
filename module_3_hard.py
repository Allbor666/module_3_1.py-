def calculate_structure_sum(structure):
    count_num = 0
    count_str = 0

    if isinstance(structure, int):
        count_num += structure
    elif isinstance(structure, str):
        count_str += len(structure)
    elif isinstance(structure, (list, tuple, set)):
        for item in structure:
            count_num += calculate_structure_sum(item)
    elif isinstance(structure, dict):
        for key, value in structure.items():
            count_num += calculate_structure_sum(key)
            count_str += calculate_structure_sum(value)

    return count_num + count_str

data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)
