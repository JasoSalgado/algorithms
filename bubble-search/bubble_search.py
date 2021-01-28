"""
Método de ordenamiento burbuja
Revisa cada elemento de la lista con el siguiente elemento intercambiándolos de posición si están en el orden equivocado

Ejemplo:
    4 2 6 8 5 7
    2 4 6 8 5 7
    2 4 6 5 8 7
    2 4 6 5 7 8
    2 4 5 6 7 8
"""

list = [4, 2, 6, 8, 5, 7]

# We need two forloops:
# The first loop controls how many times has to go through the list
# The second loop goes through index by index less 1 number

for i in range(len(list)):
    for x in range(len(list) - 1):
        # if compares the current element with the current element plus 1
        if list[x] > list[x + 1]:
            # aux saves the current element of the list, in this case is the index 0 which value is the number 4
            aux = list[x]
            # list[x] has the current value and then, we go to the next number that is 2
            list[x] = list[x+1]
            # aux is equal to the current value in this case 2
            list[x+1] = aux
            print(list)
