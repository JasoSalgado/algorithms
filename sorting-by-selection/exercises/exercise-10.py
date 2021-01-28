"""
Sorting by selection
"""

list = [12, 13, 26, 7, 21, 16, 29, 12, 13, 36, 26, 21, 29, 19, 49, 19, 37, 10, 32, 11, 20, 20, 15, 13, 30, 23, 16, 47, 18, 8, 33, 28, 43, 18, 16, 25, 39, 7, 31, 1, 5, 28, 44, 29, 39, 23, 12, 26, 40, 8, 11, 43, 16, 24, 28, 43, 10, 47, 22, 12, 6, 6, 35, 26, 30, 27, 23, 12, 32, 6, 14, 26, 12, 16, 5, 21, 17, 29, 4, 32, 5, 19, 45, 25, 2, 46, 17, 44, 5, 41, 23, 1, 20, 20, 14, 12, 23, 18, 28, 9]
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
