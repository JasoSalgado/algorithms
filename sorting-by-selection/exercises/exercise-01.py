"""
Sorting by selection exercise 01
"""

list = [100, 90, 80, 70, 90, 39, 645, 346, 356, 754]
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
