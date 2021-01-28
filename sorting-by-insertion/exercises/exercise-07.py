"""
Sorting by insertion
"""

list = [49, 19, 17, 19, 3, 28, 29, 28, 27, 42, 1, 28, 48, 14, 33]
print(f"List: {list}")

for i in range(1, len(list)):
    aux = list[i]
    j = i - 1

    while j >= 0 and aux < list[j]:
        list[j + 1] = list[j]
        list[j] = aux
        j -= 1

print(list)
