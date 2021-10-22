import random as r
import time as t

strength = 1
rp = 0
cash = 0
intellegence = 0
print(
    "you are young and you are walking down castle town and you stumble apon a newspaper. 'KNIGHT SAVES CASTLE TOWN FROM MONSTERS' the newspaper says, it reminds you of your dream of being a knight when you grow up"
)
print()
print(
    "Then your parents got a job as servants for the king and queen so now you live in the castle"
)
print()
print(
    "your parents also allow you to buy something because its your birthday. You can decide. because you want to be a famous knight when you grow up, you decide between two things. a wooden sword or a training station"
)
print()
choice1 = input('sword or training station ')
if choice1 == "sword":
    print(
        "You choose sword. you get 0.25 strength and 1 intellegence every time you try to swing"
    )
if choice1 == "training station":
    print(
        "you choose training station you get 0.025 strength and 0.50 intellegence every second you train"
    )
else:
    print("you chose to save your money")
choice2 = input("do you want to use your item you bought? ")
remember1 = choice1
choice3 = 'yes'
if choice2 == "yes":
    while choice1 == "sword" and choice3 == "yes":
        t.sleep(5)
        strength += 0.25
        intellegence += 1
        choice3 = input("do you want to train again ")
if choice3 != "yes":
    choice1 = ""
while choice1 == "training station" and choice3 == "yes":
    t.sleep(1)
    strength += 0.025
    intellegence += 0.50
    choice3 = input("do you want to train again ")
if choice3 != "yes":
    choice1 = ""
print()
print(
    "tommorow is the princess's birthday and you get to meet the princess because of your dad"
)
print()
print(
    "now you are 16 and you are a knight. your dream is working for the king protecting the castle"
)
print("then out of nowhere a horde of monsters appear")
choice4 = int(
    input(
        "how many monsters do you kill (the more you kill, the longer it will take and the more money you get and the more credit )"
    ))

t.sleep(choice4 / (strength * strength))
rp += choice4
if choice4 >= 10:
    cash += 100
print(
    "king: you have fought bravely young knight you might have the power to protect my daughter have $100"
)
print("a few months later you start you form a friendship with the princess")
print()
print(
    "the calamity is starting to get closer and closer the princess still has not awaken her power you are starting to protect the princess and they want to go to the korok forest to clear the monsters "
)
print()
choice5 = input(
    "do you want to go to korok forest or stay and work on the guardians and train (go/stay)"
)

if choice5 == "go" and strength > 2:
    print(
        "you went to the korok forest which was infested with monsters but you killed them all then you got to	 the master sword but there was astor which wanted to kill the princess malice type of your allys appeared and broke your sword you get launched back and when they malice allys were about to attack the princess the master sword woke up and sealed the malice you look back and you try to pull the sword it was hurting your hand right when you were about to give up it popped out"
    )
elif choice5 == "go" and strength < 2:
    print(
        "you went to the korok forest and the monsters came and overpowered you."
    )
	t.sleep(5)
	print("YOU DIED")
	print("RIP")
if choice5 == "stay" and intellegence > 4:
    print(
        "you work on guardians while your allys went to korok forest you studied them one turned on you think what if one gets currupted so you expirmented on one of the cores you pick up some malice and some chemicals and the chemicals desolved the malice and you fused the chemicals you made to the core and you pour some malice on and it deflected it you put the core back in the guardian "
    )
