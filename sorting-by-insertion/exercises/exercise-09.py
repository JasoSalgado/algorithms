"""
Sorting by insertion
"""

list = [34, 43, 18, 32, 3, 25, 27, 11, 24, 40, 42, 37, 36, 48, 14]
print(f"List: {list}")

for i in range(1, len(list)):
    aux = list[i]
    j = i - 1

    while j >= 0 and aux < list[j]:
        list[j + 1] = list[j]
        list[j] = aux
        j -= 1
print(list)
