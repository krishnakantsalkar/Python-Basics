import random


playerhp = 200
enemyatk1 = 40
enemyatk2 = 80


while playerhp > 0:
    dmg = random.randrange(enemyatk1, enemyatk2)
    playerhp = playerhp - dmg
    if playerhp <= 0:
        # pass keyword to leave the conditional code empty
        playerhp = 0
    if dmg > 70:
        print("Enemy did", dmg, "points of damage",
              "It was Super Effective!", "hp left:", playerhp)
# continue keyword to skip code below and start from top
    else:
        print("Enemy did", dmg, "points of damage.", "current hp is:", playerhp)
