"""
Sorting by insertion
"""

list = [43, 9, 37, 4, 15, 37, 3, 31, 29, 47, 2, 3, 40, 47, 36]
print(f"List: {list}")

for i in range(1, len(list)):
    aux = list[i]
    j = i - 1

    while j >= 0 and aux < list[j]:
        list[j + 1] = list[j]
        list[j] = aux
        j -= 1
print(list)
