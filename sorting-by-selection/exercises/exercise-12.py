"""
Sorting by selection
"""

list = [7, 22, 26, 4, 27, 20, 26, 39, 43, 25, 18, 22, 40, 19, 27, 35, 36, 13, 26, 42, 2, 24, 19, 20, 2, 15, 1, 29, 30, 48]
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
