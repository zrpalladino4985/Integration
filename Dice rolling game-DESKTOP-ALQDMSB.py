import random


def rollDice():
    """

    :return: 
    """
    global swordBuff
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    diceSum = dice1 + dice2
    print("You rolled a", str(dice1), "and a",
          str(dice2) + " and together got a(n)", str(diceSum) + ".")
    if swordBuff == True:
        diceSum += 1
        print("Your sword adds 1 to your dice roll and your roll is now",
              str(diceSum) + ".")
    return diceSum


def reduce():
    """

    """
    global numLives
    numLives -= 1
    print("You lost a life! you only have", numLives, "lives left.")


def lootChance(coin1, coin2):
    """

    :param coin1: 
    :param coin2: 
    :return: 
    """
    global goldAmt
    global swordBuff
    global numLives
    x = random.randint(1, 100)
    if x <= 80:
        gold = random.randint(coin1, coin2)
        goldAmt += gold
        print("You gained", str(gold),
              "gold from that fight, and you now have", str(goldAmt),
              "gold in total.")
    elif x <= 95:
        print("You picked up a sword from the battle!")
        swordBuff = True
        return swordBuff
    elif x <= 100:
        numLives += 1
        print("You got an extra life!")
        print("You now have", numLives, "lives left.")
        return numLives


def user_option(runChance, atkChance):
    """

    :param runChance: 
    :param atkChance: 
    """
    global scoreTotal
    x = input("what are you going to do? attack(a), run away(r) ")
    h = rollDice()
    if x == "a":
        if h >= atkChance:
            print("You won!")
            lootChance(4, 9)
            scoreTotal += (runChance + atkChance) / 2
        else:
            print("You lost.")
            reduce()
    if x == "r":
        if h >= runChance:
            print("You got away safely!")
        else:
            print("You didn't get away safely.")
            reduce()


def randSenario():
    """

    :rtype: object
    """
    x = random.randint(1, 4)
    # number of integers is the number of senarios
    if x == 1:
        senarioForrest()
    elif x == 2:
        senarioPlains()
    elif x == 3:
        senarioRuins()
    elif x == 4:
        senarioTundra()


def senarioForrest():
    """
    :rtype: object

    """
    print("You have entered a forrest.")
    x = random.randint(1, 10)
    if x in range(1, 11):
        print(
            "A werewolf has come out from behind the trees, and it doesn't "
            "look very friendly!")
        userOption(3, 7)


def senarioTundra():
    """

    """
    print("You have entered a tundra.")
    print("A polar bear has come out from its den, and hes big!")
    userOption(3, 8)


def senarioPlains():
    """

    """
    print("Plains")
    print("A sentient tree sprouted from the ground and is trying to mess "
          "you up!")
    userOption(3, 8)


def senarioRuins():
    """

    """
    print("Ruins")
    print("You hear rattling as some skeletons in armor come from the ruined "
          "structures and attack you!")
    userOption(4, 8)


scoreTotal = 0
goldAmt = 0
numLives = 5
swordBuff = False

print("Welcome to my adventure game!")
# print("You will go through different lands and areas to get to the final obsstical, a fierce dragon!")
print("You will have 5 lives to get through the the adventure")
print(" ")

while numLives != 0:
    randSenario()
print("Your total score was:", float(scoreTotal))
