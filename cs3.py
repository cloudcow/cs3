import time
import random

def attack(team):
    extraDamage = headshootAttempt(team)
    return random.randrange(25) + extraDamage

def headshootAttempt(team):
    chance = random.randrange(100)
    if chance > 90:
        print(f"{team} did HEADSHOOOOT!!!!!! for {chance} DMG!")
        return chance
    else:
        return 0

def isThereWinner(counterTerroristHealth, terroristHealth):
    if counterTerroristHealth < 1:
        print("Counter-Terrorists win!")
        return True
    if terroristHealth < 1:
        print("Terrorists win!")
        return True
    return False

dmg = random.randrange(25)
dmg2 = random.randrange(25)
counterTerroristHealth = 100
terroristHealth = 100
counterTerroristHealth = counterTerroristHealth - dmg
terroristHealth = terroristHealth - dmg2

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
    print(f"Counter-Terrorist health: {counterTerroristHealth} ")
    print(f"Terrorist health: {terroristHealth}" )
    print("------------------------------")
    dmg = attack("Counter-Terrorist")
    dmg2 = attack("Terrorist")
    counterTerroristHealth = counterTerroristHealth - dmg
    terroristHealth = terroristHealth - dmg2
    gameOver = isThereWinner(counterTerroristHealth, terroristHealth)
    if (gameOver):
        break
