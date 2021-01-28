"""
Binary search exercise 07
"""

list = [49, 74, 89, 106, 127, 152, 155, 157, 183, 195, 195, 207, 232, 250, 264, 273, 274, 276, 324, 367, 396, 458, 488, 489, 499, 500, 503, 532, 577, 628, 630, 648, 650, 656, 674, 679, 693, 694, 698, 789, 794, 807, 836, 838, 886, 897, 898, 901, 910, 956]
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
        return f"We found {data_to_search} in its position {binary_search(data_to_search)}"

for i in range(len(list)):
    print(f"Index: {i}  => {list[i]}")

print(search(183))
