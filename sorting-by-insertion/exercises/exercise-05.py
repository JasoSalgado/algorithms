"""
Sorting by insertion
"""

list = [45, 26, 1, 10, 20, 14, 25, 40, 26, 4, 43, 39, 33, 14, 24, 46, 16, 17, 2, 30, 1, 29, 35, 26, 30, 48, 49, 2, 30, 40]
print(f"List: {list}")

for i in range(1, len(list)):
    aux = list[i]
    j = i - 1

    while j >= 0 and aux < list[j]:
        list[j + 1] = list[j]
        list[j] = aux
        j -= 1
print(list)
