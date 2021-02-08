# Algorithms with Python

### An algorithm is the list of instructions and rules that a computer needs to do to complete a task
#### List of data structures you can consult here: 

 ### binary-search   
### bubble-search
### linear-search
### pile
### sorting-by-insertion
### sorting-by-selection

## Binary Search Example

"""
Binary search exercise 01
"""

    list = [30, 111, 120, 146, 290, 293, 343, 350, 357, 492]
    print(f"***** {list} *****")
    
    def binary_search(data_to_search):
        left = 0
        right = len(list) - 1

	    while left <= right:
        # We find the middle point with this while loop
	        middle = (left + right) // 2

	        # We search the data
	        if data_to_search == list[middle]:
	            return middle
	        elif data_to_search < list[middle]:
	            right = middle - 1
	        else:
	            left = middle + 1
	    return None


    def search(data_to_search):
	    if binary_search(data_to_search) == None:
	        return f"We could not find the data {data_to_search}"
        else:
	        return f"We found the data {data_to_search} in its index {binary_search(data_to_search)}"
    
    
    print("Going through the list: ")
    for i in range(len(list)):
        print(f"{i} => {list[i]}")
    
    print(search(1000))





##### These examples have not been completed yet. I am working on them.



