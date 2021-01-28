"""
Binary search exercise 08
"""

list = [101, 154, 179, 233, 237, 263, 275, 288, 300, 373, 387, 431, 458, 483, 556, 603, 635, 650, 680, 683, 715, 802, 889, 925, 997]

print(f"***** {list} *****")

def binary_search(data_to_search):
    left = 0
    right = len(list) -1

    while left <= right:
        middle = (left + right) // 2

        if data_to_search == list[middle]:
            return middle
        elif data_to_search < list[middle]:
            right = middle - 1
        else:
            data_to_search = middle + 1
    return None


def search(data_to_search):
    if binary_search(data_to_search) == None:
        return f"Not found {data_to_search}"
    else:
        return f"We found {data_to_search} in its position {binary_search(data_to_search)}"


for i in range(len(list)):
    print(f"Index: {i} => {list[i]}")


print(search(101))
