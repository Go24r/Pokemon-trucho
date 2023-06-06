#!/usr/bin/env python3

#=----IMPORTS----=
import os
from random import randint

#=----CONSTS----=
VIDA_INICIAL_PIKACHU = 100
VIDA_INICIAL_SQUIRTLE = 100


#=----DEFS----=
def draw_stats():
    global vida_pikachu, vida_squirtle
    os.system("cls")
    if vida_pikachu < 0:
        vida_pikachu = 0
    if vida_squirtle < 0:
        vida_squirtle = 0
        
    barra_vida_pikachu =  int(vida_pikachu * 10 / VIDA_INICIAL_PIKACHU)
    barra_vida_squirtle = int(vida_squirtle * 10 / VIDA_INICIAL_SQUIRTLE)

    print("----------------POKEMON TRUCHO----------------") 
    print("Pikachu:   [{}{}]  ({}/{})".format("*" * barra_vida_pikachu, " " * (10 - barra_vida_pikachu), vida_pikachu,VIDA_INICIAL_PIKACHU))
    print("Squirtle:   [{}{}] ({}/{})".format("*" * barra_vida_squirtle, " " * (10 - barra_vida_squirtle), vida_squirtle,VIDA_INICIAL_SQUIRTLE))
    print("----------------------------------------------")
    
def turno_player():
    global vida_pikachu, vida_squirtle
    draw_stats()
    ataque_squirtle = None
    while ataque_squirtle != "p" and ataque_squirtle != "a" and ataque_squirtle != "b" and ataque_squirtle != "n":
        
        draw_stats()
        print("Es el turno de Squirtle, elige una opción:")
        print("-[P] Placaje")
        print("-[A] Pistola Agua")
        print("-[B] Burbujas")
        print("-[N] Nada")
        ataque_squirtle = input("Tu opción: ")
        
    match ataque_squirtle:
        case "p":
            vida_pikachu -= 10
            draw_stats()
            print("Squirtle ha usado placaje")
        case "a":
            vida_pikachu -= 12
            draw_stats()
            print("Squirtle ha usado Pistola Agua")
        case "b":
            vida_pikachu -= 9
            draw_stats()
            print("Squirtle ha usado Burbujas")
        case "n":
            draw_stats()
            print("No has hecho nada")

    input("ENTER PARA CONTINUAR...\n\n")
    os.system("cls")
    

def turno_npc():
    global vida_pikachu, vida_squirtle
    ataque_pikachu = randint(1, 2)
    if ataque_pikachu == 1:
        vida_squirtle -= 9
        draw_stats()
        print("Pikachu ha usado Bola voltio")
    else:
        vida_squirtle -= 14
        draw_stats()
        print("Pikachu ha usado Onda Trueno")
    
    input("ENTER PARA CONTINUAR...\n\n")
    os.system("cls")
        
def check_game():
    global vida_pikachu, vida_squirtle, ganador
    if vida_squirtle > 0 and vida_pikachu > 0 :
        return True;
    
    if vida_pikachu <= 0:
        draw_stats()
        ganador = "Squirtle"
        return False
    if vida_squirtle <= 0:
        draw_stats()
        ganador = "Pikachu"
        

    
def start_game():
    global vida_pikachu, vida_squirtle
        
    vida_pikachu = VIDA_INICIAL_PIKACHU
    vida_squirtle = VIDA_INICIAL_SQUIRTLE
    
    while vida_pikachu > 0 and vida_squirtle > 0:
        turno_player()
        if not check_game(): break
        turno_npc()
        if not check_game(): break
    
    draw_stats()
    print(f"¡{ganador} ha ganado!")
    input("Pulsa ENTER para empezar una nueva partida...\n\n")


#=---MAIN---=
vida_pikachu = VIDA_INICIAL_PIKACHU
vida_squirtle = VIDA_INICIAL_SQUIRTLE

while True:
    start_game()
