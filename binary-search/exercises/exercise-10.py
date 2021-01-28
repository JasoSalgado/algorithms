"""
Binary search exercise 10
"""

list = [773, 3697, 6110, 8638, 9320, 9897, 13606, 17799, 21950, 22673, 26108, 27951, 34623, 43586, 43826, 61013, 61374, 69977, 74035, 75648, 82545, 86075, 97061, 98488, 99679]
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


print(search(100))
