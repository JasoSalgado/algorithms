"""
Binary search exercise 03
"""

list = [10, 14, 37, 58, 106, 153, 161, 174, 279, 293, 332, 337, 345, 369, 471]
print(f"***** {list} ****")

def binary_search(data_to_search):
    left = 0
    right = len(list) - 1

    while left <= right:
        middle = (left + right) // 2

        if data_to_search == list[middle]:
            return middle
        elif data_to_search < list[middle]:
            right = middle - 1
        else:
            left = middle + 1
    return None


def search(data_to_search):
    if binary_search(data_to_search) == None:
        return f"We did not find the data {data_to_search}"
    else:
        return f"We found the data {data_to_search} in its position {binary_search(data_to_search)}"


for i in range(len(list)):
    print(f"Index {i} => {list[i]}")

print(search(174))
