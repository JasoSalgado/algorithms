"""
Bubble search exercise 07
"""

list = [543,4567,765,67887,654567,9876,54567,898765,987654,456789876,54678,99876543,56789,87654]
print(f"List: {list}")

for i in range(len(list)):
    for x in range(len(list) - 1):
        if list[x] > list[x + 1]:
            aux = list[x]
            list[x] = list[x + 1]
            list[x + 1] = aux
            print(list)

