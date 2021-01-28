"""
Binary search exercise 11
"""
list = [43881, 111225, 138784, 187616, 390488, 527791, 699262, 794787, 875416, 969470]
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
            left = middle + 1
    return None


def search(data_to_search):
    if binary_search(data_to_search) == None:
        return f"Not found {data_to_search}"
    else:
        return f"We found it {data_to_search} in its position {binary_search(data_to_search)}"

for i in range(len(list)):
    print(f"Index: {i} => {list[i]}")

print(search(0))

