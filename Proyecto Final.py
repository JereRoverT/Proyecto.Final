#Bienvenidos a mi programa integrador final de Python por DigitalMind
#En el mismo, implementé algunos de los conocimientos aprendidos en el curso
#Algunas partes tienen la funcion de time.sleep solo a modo de poner a prueba la paciencia jeje
#Librerias que requieren instalacion fueron: Matplotlib y Numpy
import time
import random
import sys
import matplotlib.pyplot as plt
import numpy as np
import string
name=input('Introduce tu nombre ')
time.sleep(0.75)
print("¡Hola", name, "! Bienvenido a mi proyecto final de Python")
time.sleep(1.25)
print("""¿Qué queres hacer? Escribe una de estas opciones
a)Jugar piedra, papel o tijera contra la máquina
b)Adivinar un número
c)Tirar un dado
d)Graficar una funcion
e)Cerrar programa""""")
opcion=input()
if opcion == 'a':
    while True:
        compu = random.randrange(1, 3)
        def ppt():
            time.sleep(1)
        print ("A continuacion jugarás piedra, papel o tijera")
        time.sleep(1)
        persona = int(input("""Selecciona. 
1= Piedra 
2= Papel 
3= Tijera 
"""))
        if compu == 1 and persona == 1:
            print("Empate")
            time.sleep(2)
            
        elif compu == 1 and persona == 2:
            print("Has ganado")
            time.sleep(2)
            sys.exit()
        elif compu == 1 and persona == 3:
            print("Has perdido")
            time.sleep(2)
            
        elif compu == 2 and persona == 1:
            print("Has perdido")
            time.sleep(2)
            
        elif compu == 2 and persona == 2:
            print("Empate")
            time.sleep(2)
            
        elif compu == 2 and persona == 3:
            print("Has ganado")
            time.sleep(2)
            sys.exit()
        elif compu == 3 and persona == 1:
            print("Has ganado")
            time.sleep(2)
            sys.exit()    
        elif compu == 3 and persona == 2:
            print("Has perdido")
            time.sleep(2)
            
        elif compu == 3 and persona == 3:
            print("Has empatado")
            time.sleep(2)
            
        else:
            print("Has ingresado un numero incorrecto")
            time.sleep(2)
            
elif opcion == 'b':
    while True:
        time.sleep(1)
        print("A continuación tendras que adivinar un número")
        time.sleep(0.75)
        print("Si el número coincide con la máquina, ganas")
        time.sleep(.75)
        maquina = random.randint(1, 10)
        persona = int(input("Elige un numero entre 1 y 10 "))
        print(maquina)
        print(persona)
        if persona == maquina:
            print("Felicidades, has ganado")
            time.sleep(3)
            sys.exit()
        else:
            print("No has acertado")
        time.sleep(1)         
elif opcion == 'c':
    while True:
        time.sleep(1)
        print("Tirando dado")
        time.sleep(0.5)
        print(".")
        time.sleep(.5)
        print("..")
        time.sleep(.5)
        print("...")
        time.sleep(.5)
        dado = random.randrange(1, 6)
        print("El dado ha caído en", dado)
        time.sleep(3)
        print("Hasta luego")
        time.sleep(2)
        break
elif opcion == 'd':
    time.sleep(1)
    print("Un gráfico será generado")
    time.sleep(0.75)
    x = np.linspace(0, 5, 3, 8)
    y = 5 + 2 * np.sin(x * 2)

    fig, ax = plt.subplots()
    ax.plot(x, y, linewidth=1.0)

    ax.set(xlim=(0, 5), xticks=np.arange(1, 8),
       ylim=(0, 5), yticks=np.arange(1, 8))
    plt.show()
elif opcion == 'e':
    time.sleep(.75)
    print("Nos vemos")
    sys.exit()
else:
        print("La opción no es válida")
        time.sleep(.75)
