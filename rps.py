import random
print("***********************ROCK-PAPER-SCISSORS*************************");
print("Press p for paper, r for rock, s for scissors")
game = ['r','p','s'];

while(1):
    user = input("Please enter your choice : ")
    comp = random.choice(game)
    print("computer selects : ",comp)
    if(user != comp):
        if(user == 'r' and comp == 's'):
            print("You win");
        elif(user == 's' and comp == 'p'):
            print("You win")
        elif(user == 'p' and comp == 'r'):
            print("You win")
        else:
            print("comp win")
    else:
        print("tie")
    print("press y to play more")
    ans = input();
    if(ans != 'y'):
        print("Run again to play more")
        break;
