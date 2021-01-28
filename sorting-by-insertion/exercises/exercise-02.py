"""
Sorting by insertion
"""

list = [33, 37, 34, 23, 1, 21, 6, 42, 1, 14, 16, 2, 19, 28, 34, 2, 32, 18, 35, 36, 10, 40, 7, 10, 15, 13, 8, 38, 23, 3]
print(f"List: {list}")

for i in range(1, len(list)):
    aux = list[i]
    j = i - 1
    while j >= 0 and aux < list[j]:
        list[j + 1] = list[j]
        list[j] = aux
        j -= 1

print(list)
