"""
Ordering by selection
"""

list = [185, 335, 807, 112, 406, 620, 410, 327, 76, 938]
print(f"List: {list}")

for i in range(len(list)):
    minimum = i
    for x in range(i, len(list)):
        if list[x] < list[minimum]:
            minimum = x
    aux = list[i]
    list[i] = list[minimum]
    list[minimum] = aux

    print(list)


