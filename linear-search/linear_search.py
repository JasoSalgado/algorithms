"""
Linear search

Functioning:
    We go through each element
    We compare each element that we are looking for in each element of the list
    In case we find it, we have to return the index in which was found, in other case return false or None

"""
def linear_search(data):
    # Let´s go through the list
    for x in range(len(list)):
        if list[x] == data:
            return x
    return None


def search(data):
    if linear_search(data) == None:
        return f'{data} was not found.'
    else:
        return f'{data} was found in index {linear_search(data)} '


list = [10, 45, 346, 456, 456, 756845, 8768, 46784578, 7854786]


print(search(456))
