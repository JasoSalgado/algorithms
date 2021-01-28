"""
Sorting by insertion
"""

list = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print(f"List: {list}")

for i in range(1, len(list)):
    aux = list[i] # i = 9
    j = i - 1 # j = 10
    while j >= 0 and aux < list[j]:
        list[j + 1] = list[j]
        list[j] = aux
        j -= 1
        print(f"Going through the list: {list}")
print(list)
