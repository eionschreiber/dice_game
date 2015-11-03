import random

player=input("What is your name? ")
player2=input("What is your name Player two? ")
die_one =random.randint(1,6)
die_two = random.randint(1,6)
die_three =random.randint(1,6)
die_four =random.randint(1,6)
def graphic():
        
    if (die_one, die_two, die_three, die_four) == (1):
        print("""[---------]
                 [         ]
                 [    O    ]
                 [         ]
                 [---------]""")
        print()
        
    if (die_one, die_two, die_three, die_four) ==(2):
        print("""[---------]
                 [ O       ]
                 [         ]
                 [      O  ]
                 [---------]""")
        print()
 
    if (die_one, die_two, die_three, die_four) ==(3):
        print("""[---------]
                 [ O       ]
                 [    O    ]
                 [        O]
                 [---------]""")
        print()

    if (die_one, die_two, die_three, die_four) ==(4):
        print("""[---------]
                 [  O   O  ]
                 [         ]
                 [  O   O  ]
                 [---------]""")
        print()

    if (die_one, die_two, die_three, die_four) ==(5):
        print("""[---------]
                 [ O     O ]
                 [    O    ]
                 [ O     O ]
                 [---------]""")
        print()
       
    if (die_one, die_two, die_three, die_four) ==(6):
        print("""[---------]
                 [  O   O  ]
                 [  O   O  ]
                 [  O   O  ]
                 [---------]""")
        print()
        
        
def welcome():
    print("Welcome to the Roll the Dice game!")
    return player
    return player2

def roll():
    
    con='yes'
    while con=='yes':
        v =verse()
        print(player, " rolled  ", str(die_one), " and ", str(die_two))
        print(player2, " rolled  ", str(die_three), " and ", str(die_four)) 
        print(v)
        con=input("Do you want to continue yes/no: ")
        
def verse():
    if die_one + die_two > die_three + die_four:
	    print(player, " Wins ")
    if die_three + die_four > die_one + die_two:
	    print(player2, " Wins")

def main():
    n=welcome()
    roll()
    print("Thank you for playing, ", player, " and ", player2)
   

main()