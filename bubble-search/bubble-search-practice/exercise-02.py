"""
Bubble search exercise 02
"""

list = [1456, 126, 17856, 368, 784, 152, 895, 3659 ,157 ,1879, 250, 10, 11, 485623, 36985]
print(f"List´s elements: {list}")

for i in range(len(list)):
    for x in range(len(list) - 1):
        if list[x] > list[x + 1]:
            aux = list[x]
            list[x] = list[x + 1]
            list[x + 1] = aux
            print(list)
