"""
Sorting by insertion
"""

list = [28, 49, 14, 41, 2, 5, 16, 47, 35, 32, 14, 13, 33, 2, 44]
print(f"List: {list}")

for i in range(1, len(list)):
    aux = list[i]
    j = i - 1

    while j >= 0 and aux < list[j]:
        list[j + 1] = list[j]
        list[j] = aux
        j -= 1
print(list)
