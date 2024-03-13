import time
import random

def attack(team):
    extraDamage = headshootAttempt(team)
    return random.randrange(25) + extraDamage

def headshootAttempt(team):
    chance = random.randrange(100)
    if chance > 90:
        print("{team} did HEADSHOOOOT!!!!!! for {chance} DMG!")
        return chance
    else:
        return 0

dmg = random.randrange(25)
dmg2 = random.randrange(25)
totalHealth1 = 100
totalHealth2 = 100
totalHealth1 = totalHealth1 - dmg
totalHealth2 = totalHealth2 - dmg2

print("Welcome to the Official 1v1 Counter-Strike Tournament ")
while True:
    time.sleep(1)
    print("Loading arena... ")
    time.sleep(1)
    print("Loading arena... ")
    time.sleep(1)
    print("Loading arena... ")
    time.sleep(1)
    print("Loading success! ")
    break

while True:
    print("M4/AK47 ")
    choice = input("Choose a weapon for the players: ")
    if choice == ("M4"):
        print("They are armed with M4s. ")
        break
    if choice == ("AK47"):
        print("They are armed with AK47s. ")
        break

while True:
    time.sleep(1.5)
    print("Okay lets go. ")
    time.sleep(1.5)
    print("The round has started! ")
    break

while True:
    time.sleep(1.5)
    print("The players are going A! ")
    time.sleep(1.5)
    print("... ")
    time.sleep(1.5)
    print("..." )
    break

while True:
    print("The players have met each other on A! ")
    time.sleep(1.5)
    print("The firefight has begun! ")
    break

while True:
    time.sleep(2)
    print(f"Counter-Terrorist health: {totalHealth1} ")
    print(f"Terrorist health: {totalHealth2}" )
    print("------------------------------")
    dmg = attack("Counter-Terrorist")
    dmg2 = attack("Terrorist")
    totalHealth1 = totalHealth1 - dmg
    totalHealth2 = totalHealth2 - dmg2
    if totalHealth1 < 1:
        print("Terrorists win! ")
        break
    if totalHealth2 < 1:
        print("Counter-Terrorists win! ")
        break
