"""
Sorting by selection
"""

list = [33, 13, 14, 25, 11, 29, 33, 40, 38, 11]
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
