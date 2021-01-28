"""
Binary search

Functioning:
    It looks for a data set


    Advantages:
    It makes less comparisons thatn the lineal search

    Requirements:
    It must a have a ordered list from smaller to higher

    Algorithm:
    It calculates the middle point, (left + right) / 2
    It compares the middle point with the data to search
    If it is equal to the middle point, returns index
    If data to search is higher thatn the middle point, left is equal to the middle value + 1
    If data to search is smaller thatn middle point, right is equal to the middle value - 1
    Code will execute and when left be smaller or equal to right
"""

list = [5, 12, 15, 30, 50, 65, 70, 87, 88, 96]

def binary_search(data_to_search):
    # We define the first index and the last one
    left = 0
    right = len(list) - 1

    while left <= right:
        # We calculate the middle point
        middle = (left + right) // 2 # 0 + 9 = 4.5 we round it to 4
        # We compare the data to search with the list in the middle point
        if data_to_search == list[middle]:
            # If this is true return index = middle
            return middle
        elif data_to_search < list[middle]:
            right = middle - 1
        else:
            left = middle + 1
    return None


def search_data(data_to_search):
    if binary_search(data_to_search) == None:
        return f"We did not find the data {data_to_search}"
    else:
        return f"We found the data {data_to_search} in index: {binary_search(data_to_search)}"

# we go through the list
for i in range(len(list)):
    print(f"Index: {i} ==>> {list[i]}")


print(search_data(100))

