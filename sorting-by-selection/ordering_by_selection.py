"""
Ordering by selection
This algorithm orders elements from ascending to descending
Functioning:
    It looks for the smallest element
    Interchange it by the current one
    It folows looking for the smallest element in the list
    Interchange it by the current one
    This is a repetitive operation

index =    0 1 2 3 4 5 6

Elements = 4 2 6 8 5 7 0
           0 2 6 8 5 7 4
           0 2 4 8 5 7 4
           0 2 4 5 8 7 6
           0 2 4 5 6 7 8
"""

list = [4, 2, 6, 8, 5, 7, 0]
print(f"List: {list}")

# The forloop goes through all list
for i in range(len(list)):
    # We save in a variable the current value of i that is 4
    minimum = i
    # This forloop goes through from the current element up to all list
    for x in range(i, len(list)):
        # IF compares the smallest element of the list in this case x -index 0-= 4 and minimum = 4
        if list[x] < list[minimum]:
            # We save the value of x in the variable minimum and its value is the index 1 that is 2
            minimum = x
    # We save the current value of i that is 4
    aux = list[i]
    # list[i] saves the value of list[minimum] that means that the value of minimum is the index 1, value 2
    list[i] = list[minimum]
    # We save the current element in the variable aux
    list[minimum] = aux
    print(list)
