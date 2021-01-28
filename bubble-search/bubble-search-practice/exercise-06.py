"""
Bubble search exercise 06
"""

list = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0]
print(f"List: {list}")

for i in range(len(list)):
    for x in range(len(list) -1):
        if list[x] > list[x + 1]:
            aux = list[x]
            list[x] = list[x + 1]
            list[x + 1] = aux
            print(list)
