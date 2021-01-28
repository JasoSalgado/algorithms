"""
Sorting by selection exercise 02
"""

list = [439, 179, 603, 757, 145, 850, 518, 672, 109, 480]
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
