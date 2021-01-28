"""
Binary search exercise 09
"""

list = [1777, 7355, 11840, 15981, 31099, 41046, 43714, 49077, 49547, 54777, 56652, 66051, 69221, 71296, 71973, 72542, 73917, 76634, 76934, 78667, 78765, 84948, 88632, 91891, 99200]
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
        return f"Not found {data_to_search}"
    else:
        return f"Found it {data_to_search} in its position {binary_search(data_to_search)}"


for i in range(len(list)):
    print(f"Index: {i} => {list[i]}")

print(search(91891))
