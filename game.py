from random import randint
from time import sleep

# dificulty select
dificulty = input("select dificulty between 1 and 100 or random ")

if dificulty.upper() == "RANDOM":

    dificulty = randint(1,100)

else:
    try:

        dificulty = int(dificulty)

    except:

        dificulty = randint(1,100)

# choose starter weapon

starterWeapon = input("select starting weapon\n1 for dagger")