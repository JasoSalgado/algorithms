"""
Bubble search exercise 08
"""

list = [1111111111, 111111111, 11111111, 111111, 11111, 1111, 111, 11, 1]
print(f"List: {list}")

for i in range(len(list)):
    for x in range(len(list) - 1):
        if list[x] > list[x + 1]:
            aux = list[x]
            list[x] = list[x + 1]
            list[x + 1] = aux
            print(list)
