from generator import get_random_list

seznam = get_random_list(20, 0, 30)

def buble_sort(list_):
    repeating = len(list_) - 1
    for _ in (range(len(list_))):
        for i in range(repeating):
            if list_[i] > list_[i + 1]:
                seznam[i], seznam[i + 1] = seznam[i + 1], seznam[i]
            
    return list_

print(seznam)
print(buble_sort(seznam))
