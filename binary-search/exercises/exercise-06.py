"""
Binary search exercise 06
"""

list = [1, 13, 13, 64, 80, 81, 85, 101, 102, 104, 107, 115, 120, 128, 130, 173, 175, 181, 183, 187, 188, 201, 221, 221, 245, 247, 251, 259, 271, 293, 306, 319, 324, 329, 337, 343, 347, 350, 374, 375, 377, 379, 387, 406, 410, 414, 431, 436, 438, 489]
print(f"***** {list} ****")

def binary_search(data_to_search):
    left = 0
    right = len(list) - 1

    while left <= right:
        middle = (left + right) // 1

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
        return f"We found {data_to_search} in its position {binary_search(data_to_search)}"

for i in range(len(list)):
    print(f"Index: [i] => {list[i]}")

print(search(350))
