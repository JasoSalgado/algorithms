"""
Binary search exercise 04
"""

list = [6, 30, 34, 36, 43, 44, 45, 107, 112, 121, 151, 160, 186, 190, 191, 194, 204, 218, 233, 234, 240, 250, 259, 268, 274, 281, 303, 304, 309, 316, 319, 338, 342, 344, 349, 375, 385, 392, 401, 411, 417, 433, 438, 452, 462, 469, 476, 488, 494, 494]
print(f"***** {list} *****")

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
    print(f"Index: {i} => {list[i]}")

print(search(0))
