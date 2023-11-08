from generator import get_random_list
from copy import deepcopy

seznam = get_random_list(20, 0, 30)

def insert_sort(list):
    result = deepcopy(list)
    for index, num in enumerate(result):
        while index > 0 and num < result[index - 1]:
            result[index], result[index - 1] = result[index - 1], result[index]
            index -= 1

    return result

print(seznam)
print(insert_sort(seznam))