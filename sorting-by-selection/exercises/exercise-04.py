"""
Sorting by selection
"""

list = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print(f"List: {list}")

for i in range(len(list) - 1):
    minimum = i
    for x in range(i, len(list)):
        if list[x] < list[minimum]:
            minimum = x
    aux = list[i]
    list[i] = list[minimum]
    list[minimum] = aux

    print(list)
