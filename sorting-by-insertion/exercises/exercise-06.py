"""
Sorting by insertion
"""

list = [42, 27, 1, 30, 46, 26, 5, 49, 30, 28, 1, 33, 8, 49, 23, 38, 31, 12, 9, 9, 49, 6, 13, 14, 19, 41, 27, 40, 39, 14]
print(f"List: {list}")

for i in range(1, len(list)):
    aux = list[i]
    j = i - 1

    while j >= 0 and aux < list[j]:
        list[j + 1] = list[j]
        list[j] = aux
        j -= 1
print(list)
