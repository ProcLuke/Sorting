from generator import get_random_list
from copy import deepcopy

seznam = get_random_list(20, 0, 30)

def quick_sort(list):
    result = deepcopy(list)
    smaller = []
    bigger = []
    pivot = 0
    for num in result:
        if result[pivot] >= num:
            smaller.append(num)
        else:
            bigger.append(num)
        

