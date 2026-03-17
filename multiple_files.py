from utils import *
mensaje = input("Please type your message\n")
mensaje_volteado = flip(mensaje)
cantidad_a = count_letters(mensaje, "a")
mensaje_codificado = mensaje_volteado + str(cantidad_a)
print("Your encoded message is:", mensaje_codificado)
