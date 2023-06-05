from random import randint
vida_pikachu = 100
vida_squirtle = 100

while vida_pikachu >= 0 and vida_squirtle >= 0:
    print("Turno de pikachu")
    print("vida de pikachu {} y vida de squirtle {}".format(vida_pikachu,vida_squirtle))
    ataque_de_pikachu = randint(1, 2)
    if ataque_de_pikachu == 1:
        print("Pikachu ha usado bola voltio")
        vida_squirtle -= 10
    else:
        print("Pikachu ha usado Rayo")
        vida_squirtle -= 20

    print("Turno de Squirtle")
    ataque_de_squirtle = input("Que deseas hacer? Pistola [A]gua, [B]urbujas, [P]lacaje")
    if ataque_de_squirtle == "P":
        print("has usado Placaje")
        vida_pikachu -= 10

    elif ataque_de_squirtle == "A":
        print("has usado Placaje")
        vida_pikachu -= 15

    elif ataque_de_squirtle == "B":
        print("Has usado Burbujas")
        vida_pikachu -=20

    print("Vida de Pikachu {} - - - - - - Vida de Squirtle {}".format(vida_pikachu,vida_squirtle))