"""
Sorting by selection
"""

list = [12345, 76543, 45678, 9876, 456, 32, 12, 2435, 876]
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
