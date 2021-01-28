"""
Sorting by insertion
"""

list = [432, 211, 40, 380, 80, 428, 179, 475, 410, 45, 467, 488, 231, 221, 345]
print(f"List: {list}")

for i in range(1, len(list)):
    aux = list[i]
    j = i - 1

    while j >= 0 and aux < list[j]:
        list[j + 1] = list[j]
        list[j] = aux
        j -= 1
print(list)
