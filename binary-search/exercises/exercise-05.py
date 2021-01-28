"""
Binary search exercise 05
"""

list = [12, 21, 28, 30, 37, 40, 41, 45, 46, 49, 56, 56, 69, 80, 81, 107, 108, 118, 154, 164, 168, 179, 233, 236, 246, 258, 271, 303, 315, 341, 348, 359, 361, 370, 373, 383, 397, 404, 412, 413, 434, 435, 438, 444, 462, 468, 468, 482, 486, 490]
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
        return f"We found data {data_to_search} in its position {binary_search(data_to_search)}"


for i in range(len(list)):
    print(f"Index: {i} => {list[i]}")


print(search(1000))

