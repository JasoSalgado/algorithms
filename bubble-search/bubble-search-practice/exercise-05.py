"""
Bubble search exercise 05
"""

list = [7654, 3456, 9876, 34567, 987654, 2345, 123546, 9876, 765, 987, 9876, 3456, 987654, 23456, 6543, 23456876, 5]
print(f"List´s elements: {list}")

for i in range(len(list)):
    for x in range(len(list) - 1):
        if list[x] > list[x + 1]:
            aux = list[x]
            list[x] = list[x + 1]
            list[x + 1] = aux
            print(list)
