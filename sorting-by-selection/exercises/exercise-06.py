"""
Sorting by selection
"""

list = [987, 567, 456, 2345, 765, 8765, 4, 346, 35, 78, 5, 5]
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
