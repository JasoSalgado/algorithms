"""
Binary search
"""

list = [9, 53, 65, 186, 220, 227, 228, 235, 245, 262, 284, 375, 439, 488, 497]

def binary_search(data_to_search):
    left = 0
    right = len(list) - 1

    while left <= right:
        middle = (left + right) // 2

        if data_to_search == list[middle]:
            return middle
        elif data_to_search < list[middle]:
            right = middle -1
        else:
            left = middle + 1
    return None


def search(data_to_search):
    if binary_search(data_to_search) == None:
        return f"We could not find the data {data_to_search}"
    else:
        return f"We found the data {data_to_search} in its position {binary_search(data_to_search)}"

for i in range(len(list)):
    print(f"Index: {i} => {list[i]}")


print(search(0))
