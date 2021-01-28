"""
Bubble search exercise 03
"""

list = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print(f"List´s elements {list}")

for i in range(len(list)):
    for x in range(len(list) - 1):
        if list[x] > list[x + 1]:
            aux = list[x]
            list[x] = list[x + 1]
            list[x + 1] = aux
            print(list)
