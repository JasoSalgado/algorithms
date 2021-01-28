"""
Linear search
"""

list = [10, 9, 8, 49, 450, 3450, 345, 123, 12424, 535645, 746, 756, 75]

def linear_search(data):
    for x in range(len(list)):
        if list[x] == data:
            return x
    return None


def search(data):
    if linear_search(data) == None:
        return f"{data} was not found"
    else:
        return f"{data} was found in the index {linear_search(data)}"

print(search(123))
