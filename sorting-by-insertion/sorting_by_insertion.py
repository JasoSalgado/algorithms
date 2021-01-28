"""
Sorting by insertion

Functioning:
    We start from the index 1 so, the second element of the list
    We go through each element in the list
    Each element of the list is ordered if the number in its position left is smaller than the current element
    If the step before is right, we interchange values
    The element goes through the left until it has a smaller number

index   0  1 2  3  4 5
list    5 10 3 12 10 6
        5 3 10 12 10 6
        3 5 10 12 10 6
        3 5 10 10 12 6
        3 5 10 10 6 12
        3 5 10 6 10 12
        3 5 6 10 10 12
"""

list = [5, 10, 3, 12, 10, 6]
print(f"List: {list}")

# We start from the index 1 and are going to go through all the list
for i in range(1, len(list)):
    # We save the value of the index in a variable aux
    aux = list[i]
    # We save value of i less one element in j that is equal to 0
    j = i - 1

    # We use a while loop and will execute the code as long as both conditions are met
    # If j is higher or equal than 0 or the current value aux is smaller than its foregoing position
    while j >= 0 and aux < list[j]:
        # We increase j + 1, because the current value of j is 0, so in this case j is going to value 1
        list[j + 1] = list[j]
        # The current value of j is 1 that means it is the foregoing value
        list[j] = aux
        # We decrease j
        j -= 1

        print(list)




