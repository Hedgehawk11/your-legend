import random as r #random
import time as t
import sys as stop #program stopper
var = 0
strength = 1
rp = 0
cash = 0
intellegence = 10
is_alive = 1
choice2 = 'yes'
numMonsters = r.randint(1,1000)
name = input("\u001b[35madd your name so we can use it later ")
#add color "\u001b[??m"
print(
    "\u001b[34myou are young and you are walking down castle town and you stumble apon a newspaper. 'KNIGHT SAVES CASTLE TOWN FROM MONSTERS' the newspaper says, it reminds you of your dream of being a knight when you grow up"
)
print()

print(
    "\u001b[33mThen your parents got a job as servants for the king and queen so now you live in the castle"
)
print()
print(
    "\u001b[32myour parents also allow you to buy something because its your birthday. You can decide. because you want to be a famous knight when you grow up, you decide between two things. a wooden sword or a training station"
)
print()
choice1 = input('\u001b[31msword or training station ')
if choice1 == "sword":
    print(
        "\u001b[32mYou choose sword. you get 0.25 strength and 5 intellegence every time you try to swing"
    )
elif choice1 == "training station":
    print(
        "\u001b[33myou choose training station you get 0.1 strength and 0.5 intellegence every second you train"
    )
else:
    print("\u001b[34myou chose to save your money")
choice2 = input("\u001b[35mdo you want to use your item you bought? ")
remember1 = choice1
choice3 = 'yes'
if choice2 == "yes" or choice2=="" or choice2=="y":
    while choice1 == "sword" and choice3 == "yes":
        t.sleep(5/(((strength+intellegence)/3)+1))
        strength += 0.25
        intellegence += 5
        choice3 = input("\u001b[34mdo you want to train again (also you could hit enter)")
elif choice2 != "yes" or choice2 !="" or choice2!="y":
    choice1 = ""
if choice2 == "yes" or choice2=="" or choice2=="y":
    while choice1 == "training station" and choice3 == "yes" or choice3=='' or choice3 =='y':
        t.sleep(5/(((strength+intellegence)/3)+1))
        strength += 0.25
        intellegence += 5
        choice3 = input("\u001b[34mdo you want to train again (also you could hit enter)")
elif choice2 != "yes" or choice2 !="" or choice2!="y":
    choice1 = ""

print()
print(
    "\u001b[32mtommorow is the princess's birthday and you get to meet the princess because of your dad"
)
print()
print(
    "\u001b[31mnow you are 16 and you are a knight. your dream is working for the king protecting the castle"
)
print()
print("\u001b[32mthen out of nowhere a horde of monsters appear")
print("\u001b[33mhow many monsters do you kill (the more you kill, the longer it will take and the more money you get and the more credit) (it will take you",1000/(((strength+intellegence)/3)+1),"seconds to kill 1000")
choice4 = int(input())
    
    

t.sleep(choice4/(((strength+intellegence)/3)+1))
rp += choice4
if choice4 >= 10:
    cash += choice4*10
    print(
        "\u001b[34mking: you have fought bravely young knight you might have the power to protect my daughter have $"+str(cash)
    )
print("\u001b[35ma few months later you start you form a friendship with the princess")
print()
print(
    "\u001b[34mthe calamity is starting to get closer and closer the princess still has not awaken her power you are starting to protect the princess and they want to go to the korok forest to clear the monsters + 4 strength or stay and work on the guardians + 3 intellegence"
)
print()
choice5 = input("(go/stay)")

if choice5 == "go" and strength > 2:
    print(
        "\u001b[33myou went to the korok forest which was infested with monsters but you killed them all then you got to	the master sword but there was astor which wanted to kill the princess malice type of your allys appeared and broke your sword you get launched back and when they malice allys were about to attack the princess the master sword woke up and sealed the malice you look back and you try to pull the sword it was hurting your hand right when you were about to give up it popped out"
    )
    strength += 4
elif choice5 == "go" and strength < 2 or intellegence < 2:
    print(
        "\u001b[32myou went to the korok forest and the monsters came and overpowered you."
    )
    t.sleep(5)
    print("\u001b[31mYOU DIED")
    print("\u001b[32mRIP")
    print("\u001b[33mre- run the program and get stronger to defeat the monsters hint: train 10 times for training station train 4 times for sword")
    stop.exit()
elif choice5 == "stay" and intellegence > 10:
    print(
        "\u001b[34myou work on guardians while your allys went to korok forest you studied them one turned on you think what if one gets currupted so you expirmented on one of the cores you pick up some malice and some chemicals and the chemicals desolved the malice and you fused the chemicals you made to the core and you pour some malice on and it deflected it you put the core back in the guardian "
    )
    intellegence += 5
elif choice5 == "stay" and intellegence < 2 and strength > 2:
    print(
        "\u001b[35myou just sit there wondering what is happening then the king told you to go to the korok forest so you went to the korok forest which was infested with monsters but you killed them all then you got to	 the master sword but there was astor which wanted to kill the princess malice type of your allys appeared and broke your sword you get launched back and when they malice allys were about to attack the princess the master sword woke up and sealed the malice you look back and you try to pull the sword it was hurting your hand right when you were about to give up it popped out"
    )
elif choice5 == "stay" and intellegence < 4 and strength < 2:
    print(
        "\u001b[34myou sit there wondering what is happening then the king told you to go to the korok forest so you went to the korok forest and the monsters came and overpowered you."
    )
    t.sleep(5)
    print("\u001b[33mYOU DIED")
    print("\u001b[32mRIP")
    print("\u001b[31mre- run the program to get more intellegence or strength hint: choose sword and train 4 times")
if choice5 == "stay" and intellegence > 10 and strength > 2:
    print(
        "\u001b[32myour allys came back from the korok forest they cleared the forest and barely beat astor and now the way to the master sword is cleared"
    )
    print("\u001b[33mso you and the princess were on the way to back to tke castle and monsters attacked you were chased into the korok forest you were cornerd but the master sword was there you tried to pull it but right when you were about to give up and accept defeat it popped out")
elif choice5 == "stay" and intellegence > 10 and strength < 2:
  print("so you and the princess were on the way to back to tke castle and monsters attacked you were chased into the korok forest you were cornerd you could not defeat the monsters and you died")
  t.sleep(5)
  print("YOU DIED")
  print("RIP")
  print("re-run the program and get more intellegence or strength hint:you should select stay and have enough intellegence and strength")
  stop.exit()
print()
print('1 month later')
choice6 = input("at castle: king: " + name + " do you accept being the princesses apointed knight? (yes or no this affects the end)")
if choice6 == "yes":
  print("king: well then here ye here ye you are now the appointed knight of the princess your new duty is to protect my daughter")
elif choice6 == "no":
  print("king: well we can always look for other people to be her appointed knight")
print()
print("\u001b[36mit's been 5 months and still the princess could not awaken her power they plan to go to the spring of wisdom on her birthday to see if she can awaken it there do you go with the princess + 5 friendship or stay and work on the devine beast + 6 intellegence")
choice7 = input("(go/stay) ")
if choice7 == "stay":
  print("you did the same thing you did with the guardians but the cores are HUGE so you will need more chemicals you finished before  the princess came back so you rushed to the spring of wisdom and the pricess was there praying in order to awaken the power you pat her shoulder and she stood up you supported her and she could not awaken her power and if she does not awaken her sealing power the world will come to ruin")
elif choice7=="go":
  print("you go to the spring of wisdom to pray to awaken her sealing power a bunch of monsters appear. There are",numMonsters,"monsters")
choice8 = input('do you want to run or kill them(run/kill)')
if strength >= 12:
    print("You and the princess run away halfway down the mountain a  lynel appears you try to kill the lynel the master sword woke up again and the lynel charges but you pary it sending it back you tell the princess to run and, the lynel brought out its weapon, and the fight began it swung and you flurried it you did not even know you could do that everything became slow and you rush up to the lynel and hit it five times you jump back it starts to shoot fire but, you shot an arrow at its face and knocked it down you rush and ride it stabbing it in the back as it roars in defeat")
elif choice8 == "kill":
    print('you kill ',numMonsters,'and get ', numMonsters, 'money')
    print("a  lynel appears you try to kill the lynel the master sword woke up again and the lynel charges but you pary it sending it back you tell the princess to run and, the lynel brought out its weapon, and the fight began it swung and you flurried it you did not even know you could do that everything became slow and you rush up to the lynel and hit it five times you jump back it starts to shoot fire but, you shot an arrow at its face and knocked it down you rush and ride it stabbing it in the back as it roars in defeat")
    cash += numMonsters
elif choice8 == "kill" and strength < 12:
    print("YOU DIED")
    print("RIP")
    print("re-run the program and upgrade your strength hint: hold enter when training it's OP")
    stop.exit()
print("you head to the princess which was hiding behind a rock you tell her the lynel is dead you and the princess  walk to the  castle and then BOOM there was an earthquake then you known you ran out of time the calimity is here")
if choice5 == "stay" and intellegence > 4:
  print()
  print("you run to the castle the guardians fighting the monsters and protecting the castle the calmity trying to corrupt the but since you figured the calamity will try to currupt them the guardians are imune to the malice")
print()
print('the king sees that the monsters are coming from the same place... the center of the earth')
print('[insert dun dun dunnnnnnnnnn]')
if choice5 == "go" or choice5 == "stay" and intellegence < 4 and strength > 2:
  print("you run from the guardians as they shoot you with lasers and then BOOM the laser hit your sheild and it bounced back and hit the guardian in the eye then you notice you can send back the lasers with a pary you kill 10 guardians when you start to get weak the princess saved you by awakening her power and killing all the guardians")
  print()
  print('the monsters also rickroll you')
if choice7 == "go":
  print("the devine beasts are fighting being currupted and the champions are fighting too")
if choice7 == "stay" and choice5 == "stay":
  print("the devine beasts are ready to attack the guardians are holding the monsters back you head inside the castle then calamity ganon appears as you chase it to the sanctum you fight ganon the princess awakens her power to kill ganon")
  print("ONE HOUR LATER")
  t.sleep(5)
  print("Ganon now weak you give him the final blow cutting him right through the middle you give the princess a nod so she can seal him away")
  print()
  print("now with ganon sealed the kingdom can be in peace")
  if choice6 == "yes":
    print("you and the princess are now friends you guys hang out almost everyday")
  elif choice6 == "no":
    print("after saving the kingdom you two never saw each other again")
  print()
  t.sleep(5)
  print("THE END")
if choice7 == "go":
  print("you go to the devine beasts in order to save the champions that are weak")
  print()
  t.sleep(5)
  print("you save the zora champion first")
  t.sleep(5) 
  print ("then you save the goron champion")
  t.sleep(5) 
  print("and after that you save the gorudo champion") 
  t.sleep(5)
  print("and finally you save the rito champion")
  t.sleep(5)
  print("now with the champions freed everyone can concentrate thier power on the divine beasts")
  print()
  print('now with the beasts killed the king gives you 2 tasks that you must choose from')
  if choice6 == 'yes':
    dependentchoice1 = 0
    print('task 1: go to the earth\'s core and block the monsters off')
    print()
    print('task 2: SAVE THE PRINCESS ')
    dependentchoice1 = int(input('King: HERE YE HERE YE the knight must choose from 2 tasks '))
  else:
    print('you choose the #2 task')
print()
print("you succeed in your task and all later quests and being  the princess's knight")
t.sleep(10)
print('BUT WAIT THERE\'S MORE')
t.sleep(5)
