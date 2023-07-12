import random
def game():
    global choice
    choice = input("pick a dice type: tetrahedron - t, cube - c, octahedron - o, Pentagonal trapezohedron - p, 	Dodecahedron-d ,Icosahedron - i or n for stopping:   ")
    if choice == 't':
        print("you got from the cube number: ", random.randint(1,4))
    elif choice == 'c':
        print("you got from the cube number: ", random.randint(1,6))
    elif choice == 'o':
        print("you got from the cube number: ", random.randint(1,8))
    elif choice == 'p':
        print("you got from the cube number: ", random.randint(1,10))
    elif choice == 'd':
        print("you got from the cube number: ", random.randint(1,12))
    elif choice == 'i':
        print("you got from the cube number: ", random.randint(1,20))
    else:
        print("wrong letter buddy")
game()
while choice != 'n':
    game()
