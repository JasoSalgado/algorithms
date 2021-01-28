"""
Bubble search practice

50, 30, 100, 300, 410, 540, 128
"""

list = [50, 30, 100, 300, 410, 540, 129]
print(f"*****List´s elements: {list} *****")

for i in range(len(list)):
    for x in range(len(list) - 1):
        if list[x] > list[x + 1]:
            aux = list[x]
            list[x] = list[x + 1]
            list[x + 1] = aux
            print(list)

