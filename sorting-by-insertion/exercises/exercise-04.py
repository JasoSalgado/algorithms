"""
Sorting by insertion
"""

list = [39, 48, 22, 41, 44, 40, 49, 36, 33, 23, 14, 11, 46, 32, 3, 28, 35, 6, 47, 27, 36, 29, 7, 45, 39, 4, 3, 32, 28, 21]
print(f"List: {list}")

for i in range(1, len(list)):
    aux = list[i]
    j = i - 1

    while j >= 0 and aux < list[j]:
        list[j + 1] = list[j]
        list[j] = aux
        j -= 1
print(list)
