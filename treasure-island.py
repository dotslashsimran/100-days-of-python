print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

name=input("What's your name? ")
choice1 = input(f"Hi {name}, You wake up on an abandoned Island and there's no one around you. Just a crossroad. Where do you wish to proceed? Left or Right ")
if choice1== "left" or "Left":
  choice2 = input("You find another man named Steve in your way, 6 feet, curly brown hair, dressed in a beach shirt. Steve approaches you and claims he too is stuck in this game just like you are. He wants you to come with him for rest of your journey. Keep in mind this may make your journey easier/harder. Well, do you trust Steve? How do you wish to proceed your tresaure hunt journey? with steve or alone? ")
  if choice2=="alone" or "Alone":
      print(f"You politely decline and Steve understands. Perhaps it was a wise decision. Or was it {name}? Well we'll find out soon.")
      print("You come across a river. Let's be real, after all this trek you're probably super hungry and tired. That's when you notice there's also a boat and a coconut nearby!")
      print(f"Well {name}, looks like you've hit a jackpot. You get some rest but it's pretty late now, and there's an important choice to make.")
      choice3 = input("Do you wish to stay by the river for a night? maybe build fire and a little tent from scratch? or get that boat cross that river? ")
  elif choice2=="with steve" or "With steve" or "With Steve" or "steve" or "Steve":
    print("ok well")
  else:
      print("Please enter a valid choice lol?")
elif choice1=="right" or "Right":
  print("That was a bad choice, you have been attacked by snakes. Game over.")
else:
  print("Please enter a valid choice lol?")
