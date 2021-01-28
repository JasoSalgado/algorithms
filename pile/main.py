from os import system
system("clear")

from pile_example import Pile

pile = Pile(5)

pile.push(0)
pile.push(1)
pile.push(2)
pile.push(3)

pile.show()


print(f"Size: => {pile.size}")
print(f"State: => {pile.empty}")
print(f"Top: => {pile.top}")
