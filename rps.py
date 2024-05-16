from emoji import emojize
from random import choice

r = "🪨"
p = "📰"
s = "✂️"
move_list = [r,p,s]
record = [0,0,0]

while True:
    print("[R]ock, [P]aper, [S]cissors!")
    selection = input(">> ")
    print()

    if selection.lower == "r":
        player = move_list[0]
    elif selection.lower == "p":
        player = move_list[1]
    elif selection.lower == "s":
        player = move_list[2]
    else:
        print("no")
        continue
    
    computer = choice(move_list)

    if player == computer:
        print("tie")
    if move_list[0] in [player,computer]:
        if move_list[1] in [player,computer]:
            if player == move_list[0]:
                print("lose")
            else:
                print("win")
        else:
            if player == move_list[0]:
                print("win")
            else:
                print("lose")
    else:
        if player==move_list[1]:
            print("win")
        else:
            print("lose")

    print(f"score: win")