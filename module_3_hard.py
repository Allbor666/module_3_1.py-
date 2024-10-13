def calculate_structure_sum(data_structure):
    total_sum = 0
    def recursive_sum(data):
        nonlocal total_sum
        for element in data:
            if isinstance(element, (int, float)):
                total_sum += element
            elif isinstance(element, str):
                total_sum += len(element)
            elif isinstance(element, (list, tuple, dict)):
                recursive_sum(element)
            elif isinstance(element, set):  # Added set type check
                for item in element:
                    recursive_sum([item])
    recursive_sum(data_structure)
    return total_sum
data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]
result = calculate_structure_sum(data_structure)
print(result)
