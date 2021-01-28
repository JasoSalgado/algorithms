"""
Sorting by selection
"""

list = [31, 5, 22, 25, 42, 14, 18, 6, 12, 21, 38, 9, 43, 6, 30, 10, 22, 2, 37, 5, 20, 43, 7, 25, 35, 23, 33, 8, 27, 29]
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
