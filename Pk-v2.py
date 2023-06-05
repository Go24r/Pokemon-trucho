from random import randint

vida_maxima_pikachu = 100
vida_maxima_squirtle = 100
vida_pikachu = 100
vida_squirtle = 100

while vida_pikachu > 0 and vida_squirtle > 0:
    print("Turno de Pikachu")
    print("Vida de Pikachu: {} - ".format(vida_pikachu), end="")
    barra_vida_pikachu = "#" * int((vida_pikachu / vida_maxima_pikachu) * 10)
    print("[{}]".format(barra_vida_pikachu))

    ataque_de_pikachu = randint(1, 2)
    if ataque_de_pikachu == 1:
        print("Pikachu ha usado bola voltio")
        vida_squirtle -= 10
    else:
        print("Pikachu ha usado Rayo")
        vida_squirtle -= 20

    print("Turno de Squirtle")
    print("Vida de Squirtle: {} - ".format(vida_squirtle), end="")
    barra_vida_squirtle = "#" * int((vida_squirtle / vida_maxima_squirtle) * 10)
    print("[{}]".format(barra_vida_squirtle))

    ataque_de_squirtle = input("¿Qué deseas hacer? Pistola [A]gua, [B]urbujas, [P]lacaje: ")
    if ataque_de_squirtle == "P":
        print("Has usado Placaje")
        vida_pikachu -= 10
    elif ataque_de_squirtle == "A":
        print("Has usado Pistola de Agua")
        vida_pikachu -= 15
    elif ataque_de_squirtle == "B":
        print("Has usado Burbujas")
        vida_pikachu -= 20

    print("Vida de Pikachu: {} - Vida de Squirtle: {}".format(vida_pikachu, vida_squirtle))

if vida_pikachu <= 0:
    print("¡Squirtle ha ganado!")
elif vida_squirtle <= 0:
    print("¡Pikachu ha ganado!")