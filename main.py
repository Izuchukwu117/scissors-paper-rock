import random


comp_wins=0
player_wins=0

def choose_option():
    user_choice=input("Choose Rock, Paper or Scissors: ")
    if user_choice in ["Rock","rock","r","R"]:
        user_choice="r"
    elif user_choice in ["Paper","paper","p","P"]:
        user_choice="p"
    elif user_choice in ["Scissors","scissors","s","S"]:
        user_choice="s"
    else:
        print("Not understood. Check your spelling or reply with just the first letter.")
        choose_option()
    return user_choice

def computer_option():
    comp_choice=random.randint(1,3)
    if comp_choice==1:
        comp_choice="r"
    elif comp_choice==2:
        comp_choice="s"
    else:
        comp_choice="p"
    return comp_choice

while True:
    print("")
    user_choice=choose_option()
    comp_choice=computer_option()
    print("")

    if user_choice=="r":
        if comp_choice=="r":
            print("It is a tie. You chose rock. Computer chose rock.")
        elif comp_choice=="p":
            print("You lose. You chose rock. Computer chose paper.")
            comp_wins+=1
        elif comp_choice=="s":
            print("You win!!! You chose rock. Computer chose scissors.")
            player_wins+=1
    elif user_choice=="s":
        if comp_choice=="r":
            print("You lose. You chose scissors. Computer chose rock.")
            comp_wins+=1
        elif comp_choice=="p":
            print("You win!!! You chose scissors. Computer chose paper.")
            player_wins+=1
        elif comp_choice=="s":
            print("It is a tie. You chose scissors. Computer chose scissors")
    elif user_choice=="p":
        if comp_choice=="r":
            print("You win!!! You chose paper. Computer chose rock.")
            player_wins+=1
        elif comp_choice=="p":
            print("It is a tie. You chose paper. Computer chose paper.")
        elif comp_choice=="s":
            print("You lose. You chose paper. Computer chose scissors.")
            comp_wins+=1
        print("")
        print("Player wins: "+str(player_wins))
        print("Computer wins: "+str(comp_wins))
        print("")
        user_choice=input("Continue game? Y/N")
        if user_choice in["y","Y","Yes","yes"]:
            pass
        elif user_choice in["n","N","No","no"]:
            break
        else:
            break
            
