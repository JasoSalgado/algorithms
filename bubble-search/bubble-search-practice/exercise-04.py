"""
Bubble search exercise 04
"""

list = [100, 99, 65, 36, 76, 286, 457, 746, 346, 7465, 867, 345, 345, 542, 346]
print(f"List´s elements: {list}")

for i in range(len(list)):
    for x in range(len(list) -1):
        if list[x] > list[x + 1]:
            aux = list[x]
            list[x] = list[x + 1]
            list[x + 1] = aux
            print(list)
