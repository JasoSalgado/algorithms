"""
Sorting by insertion
"""

list = [100, 90, 99, 98, 43, 6,75, 46, 87, 546]
print(f"List: {list}")

for i in range(1, len(list)):
    aux = list[i]
    j = i - 1

    while j >= 0 and aux < list[j]:
        list[j + 1] = list[j]
        list[j] = aux
        j -= 1
print(list)
