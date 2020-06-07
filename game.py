# Nice or Mean Game Python 3.7.5

def start(nice=0,mean=0,name=""):
    #gets user name
    name = describe_game(name)
    nice,mean,name = nice_mean(nice,mean,name)

"""
Check if this is a new game or not:
if yes, get user name - if no, thank user for playing again and continue game.
If do not already have user name, user is a new player so get their name.
"""

def describe_game(name):
    if name != "":
        print("\nThank you for playing again, {}!".format(name))
    else:
        stop = True
        while stop:
            if name == "":
                name = input("\nWhat is your name? \n>>> ").capitalize()
                if name != "":
                             print("\nWelcome, {}!".format(name))
                             print("\nIn this game, you will be greeted \nby several different people. \nYou can choose to be nice or mean,")
                             print("but at the end of the game your fate \nwill be sealed by your actions.")
                             stop = False
    return name

def nice_mean(nice,mean,name):
    stop = True
    while stop:
        show_score(nice,mean,name)
        pick = input("\nA stranger approaches you for a conversation.\n Will you be nice or mean?  (N/M)  \n>>>: ").lower()
        if pick == "n":
            print("\nThe stranger walks away smiling...")
            nice = (nice + 1)
            stop = False
        if pick == "m":
            print("\nThe stranger glares at you\n menacingly and storms off...")
            mean = (mean + 1)
            stop = False
    score(nice,mean,name) #pass the 3 variables to score()

def show_score(nice,mean,name):
    print("\n{}, your current total:\n ({}, Nice) and ({}, Mean)".format(name,nice,mean))

def score(nice,mean,name): #function passed the values stored in 3 variables
    if nice > 2: #if condition valid call win function passing in variables to be used
        win(nice,mean,name)
    if mean > 2: #if condition valid call lose function passing in variables to be used
        lose(nice,mean,name)
    else: #else, call nice_mean function passing in variables to be used
        nice_mean(nice,mean,name)

def win(nice,mean,name):
    print("\nNice job {}, you win!\n Everyone loves you and you've\n made lots of friends along the way!".format(name))
    again(nice,mean,name) #calls again function passing in variables to be used

def lose (nice,mean,name):
    print("\nAhhh, too bad, game over!\n{}, you live in a dirty beat-up\n van by the river, wreched and alone!".format(name))
    again(nice,mean,name) #calls again function passing in variables to be used

def again(nice,mean,name):
    stop = True
    while stop:
        choice = input("\nDo you want to play again?  (Y/N):\n>>> ").lower()
        if choice == "y":
            stop = False
            reset(nice,mean,name)
        if choice == "n":
            print("\nOh, so sad, sorry to see you go!")
            stop = False
            quit()
        else:
            print("\nEnter ( Y ) for 'YES', ( N ) for 'NO':\n>>> ")

def reset (nice,mean,name):
    nice = 0
    mean = 0
    start(nice,mean,name) #did not reset the name variable because same user playing again, will not trigger describe_game explanations

if __name__ == "__main__":
    start()
