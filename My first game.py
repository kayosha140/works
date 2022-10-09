import random
Rock ="""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

Paper="""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

Scissors= """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
while True :
    game_images=[Rock,Paper,Scissors]

    print(game_images [0],game_images [1],game_images[2])

    user_choice=int(input('what do you choose? 0 for rock,1 for paper,2 for scissors'))
    print(game_images[user_choice])
    print(40*"-")
    computer_choice=random.randint(0,2)
    print(game_images[computer_choice])
    if user_choice==2 and computer_choice==0:
        print("user win")
        print(40*"-")
    elif computer_choice==2 and user_choice==0:
        print("user lose")
        print(40*"-")
    elif user_choice > computer_choice:
        print("user win")
        print(40*"-")
    elif computer_choice > user_choice:
        print("user lose")
        print(40*"-")
    elif computer_choice == user_choice :
        print("no one win")
        print(40*"-")
    
    
