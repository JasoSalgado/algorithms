"""
Bubble search exercise 10
"""

list = [659 , 34 , 451 , 292 , 242 , 972 , 941 , 100 , 872 , 713 , 346 , 559 , 971 , 560 , 447 , 676 , 539 , 365 , 1 , 179 , 242 , 517 , 146 , 144 , 739 , 356 , 874 , 349 , 523 , 760 , 684 , 710 , 655 , 393 , 735 , 72 , 192 , 974 , 795 , 277 , 42 , 50 , 175 , 377 , 778 , 175 , 234 , 413 , 905 , 216]
print(f"List: {list}")

for i in range(len(list)):
    for x in range(len(list) - 1):
        if list[x] > list[x + 1]:
            aux = list[x]
            list[x] = list[x + 1]
            list[x + 1] = aux
            print(list)
