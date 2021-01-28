"""
Sorting by selection
"""

list = [15, 13, 4, 31, 30, 18, 29, 42, 21, 29]
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
