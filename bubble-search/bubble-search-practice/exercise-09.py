"""
Bubble search exercise 09
"""
list = [6514 , 2352 , 3984 , 3596 , 2445 , 5535 , 6332 , 5346 , 617 , 3976 , 1242 , 2573 , 7772 , 9324 , 4655 , 3144 , 6233 , 2287 , 6109 , 4139 , 2030 , 6734 , 1495 , 9466 , 6893 , 9336 , 963 , 4412 , 5347 , 2565 , 7590 , 5932 , 6747 , 7566 , 2456 , 9982 , 8880 , 6816 , 9415 , 2426 , 5892 , 5074 , 1501 , 9445 , 6921 , 545 , 4415 , 9516 , 6426 , 7369]
print(f"List: {list}")

for i in range(len(list)):
    for x in range(len(list) - 1):
        if list[x] > list[x + 1]:
            aux = list[x]
            list[x] = list[x + 1]
            list[x + 1] = aux
            print(list)
