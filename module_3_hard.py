def calculate_structure_sum(obj):
    total_sum = 0
    if isinstance(obj, int):
        return obj
    if isinstance(obj, str):
        return len(obj)
    if isinstance(obj, dict):
        obj = list(obj.items())
    for i in obj:
        total_sum = total_sum + calculate_structure_sum(i)
    return total_sum


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 55))}])
]

result = calculate_structure_sum(data_structure)
print(result)