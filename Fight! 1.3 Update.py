from time import sleep
import random

inventory = ["Apple", "Apple"]
user_hp = 100         #Default value is 100
max_hp = user_hp      #Default value is user_hp
enemy_hp = 200        #Default value is 200
game_start = False    #Default value is False
game_over = False     #Default value is False
wait_time = 0.5       #Default value is 0.4
txt_speed = 0.05      #Default value is 0.04
difficulty = "Normal" #Default value is "Normal"
fast_mode = False     #Default value is False
confidence = 0        #Default value is 0
tutorial_done = False #Default value is False
hard_unlocked = False #Default value is False
got_apple = False     #Default value is False
enemy_turn = False    #Default value is False

#The amount of time you wait between lines of text.
if fast_mode:
    wait_time = 0.1
    txt_speed = 0.01

def wait():
    sleep(wait_time)
    
def border():
    print("---------------------------")
    wait()

def new_menu():
    for i in range(60):
        print("")
    
#Slowly types the words to make it look smoother and let the
#reader read the text slower.
def type_it(str):
    for letter in str:
        print(letter, end='', flush = True)
        sleep(txt_speed)
    print("")
    wait() 
def print_s(str):
    for letter in str:
        print(letter, end='', flush = True)
        sleep(txt_speed)
    print("")
def print_d(str):
    for letter in str:
        print(letter, end='', flush = True)
        sleep(txt_speed)
def print_e(str):
    for letter in str:
        print(letter, end='', flush = True)
        sleep(0.8)
    print("")
def voice(str):
    for letter in str:
        print(letter, end='', flush = True)
        sleep(0.1)
    print("")
    sleep(1)
    
#Checks if the player won or lost, then breaks the list if so.
#Sets win value to true or false depending on health.

'''
This function takes in the players health and the enemy's health. If the
player's health is 0 or less, it returns False, meaning the player lost. 
If the enemy's health is 0 or less, it returns True, meaning the player
won.
'''
def check_win(player, enemy):
    global game_over
    if player <= 0:
        game_over = True
        return False
    if enemy <= 0:
        game_over = True
        return True

#Checks if player can heal themself, then does so if can.
def eat():
    global user_hp
    if user_hp < max_hp:
        try:
            inventory.pop()
            heal_num = 30
            if user_hp + heal_num >= max_hp:
                user_hp = max_hp
            else:
                user_hp = user_hp + heal_num
            type_it("You eat an Apple")
            type_it("You are now at " + str(user_hp) + " HP!")
            if user_hp == max_hp:
                type_it("Your HP is maxed out!")
        except:
            type_it("You have no Apples left!")
    else:
        type_it("You are already at full HP!")
def heal():
    global user_hp
    global confidence
    if user_hp < max_hp:
        heal_num = random.randint(30, 50)
        c_num = random.randint(3, 5)
        if user_hp + heal_num >= max_hp:
            user_hp = max_hp
        else:
            user_hp = user_hp + heal_num
        type_it("You gather your confidence and...")
        type_it("You are now at " + str(user_hp) + " HP!")
        confidence -= c_num
        if user_hp == max_hp:
            type_it("Your HP is maxed out!")
    else:
        type_it("You are already at full HP!")
    
def get_apple():
    global user_hp
    global got_apple
    global inventory
    if difficulty == "Hard":
        if user_hp < 50 and got_apple == False:
            border()
            print_s("By sheer luck, you noticed")
            print_s("you have a spare Apple in")
            type_it("your backpack.")
            border()
            inventory.append("Apple")
            eat()
            got_apple = True

#Takes enemy's health when it is the player's turn.
def user_attack():
    global enemy_hp
    damage = random.choice("mnnnnnnncc")
    if damage == "n":    
        damage_num = random.randint(8, 12)
        enemy_hp -= damage_num
        type_it("Hit! Your foe lost " + str(damage_num) + " HP!")
    if damage == "c":
        damage_num = random.randint(20, 30)
        enemy_hp -= damage_num
        print_s("A critical hit!")
        type_it("Your foe lost " + str(damage_num) + " HP!")
    if damage == "m":
        type_it("Miss! Your foe lost no HP!")
        
def gain_confidence():
    global confidence
    c_num = random.choice("ooooooott")
    if confidence == 9:
        c_num = "o"
    if confidence <= 10:
        if c_num == "o":
            confidence += 1
        if c_num == "t":
            confidence += 2
    if confidence > 10:
        confidence = 10
    
def destroy():
    global enemy_hp
    global confidence
    damage = random.randint(1, 10)
    damage_num = random.randint(100, 120)
    c_num = random.randint(5, 10)
    print_d("A swing and a")
    print_e("...")
    if damage == 1:
        type_it("Miss!")
        confidence -= c_num
        print_s("Your confidence went down")
        type_it("to " + str(confidence))
    else:
        type_it("Hit!")
        enemy_hp -= damage_num
        confidence -= c_num
        type_it("Your foe lost " + str(damage_num) + " HP!")
        print_s("Your confidence went down")
        type_it("to " + str(confidence))
        
#Takes player's health when it is the enemy's turn.
def enemy_attack():
    global user_hp
    damage = random.choice("mnnnnnnnnc")
    if damage == "n":
        damage_num = random.randint(8, 12)
        user_hp -= damage_num
        type_it("You lost " + str(damage_num) + " HP!")
    if damage == "c":
        damage_num = random.randint(20, 30)
        user_hp -= damage_num
        print_s("A critical hit!")
        type_it("You lost " + str(damage_num) + " HP!")
    if damage == "m":
        type_it("Miss! You lost no HP!")

def status():
    sleep(0.2)
    new_menu()
    print("===========================")
    print("Your Health: " + str(user_hp) + " / " + str(max_hp))
    wait()
    print("Enemy Health: " + str(enemy_hp) + " / " + str(enemy_max))
    wait()
    print("Inventory: " + str(inventory))
    wait()
    print("Confidence: " + str(confidence))
    wait()
    print("[Fight] [Eat] [Heal] [Destroy]")

def restart_game():
    global difficulty
    game_start = False
    game_over = False
    if difficulty == "Easy":
        global inventory
        user_hp = 100
        max_hp = 100
        enemy_hp = 100
        inventory = ["Apple", "Apple"]
    elif difficulty == "Normal":
        user_hp = 100
        max_hp = 100
        enemy_hp = 200
        inventory = ["Apple", "Apple", "Apple"]
    elif difficulty == "Hard":
        user_hp = 250
        max_hp = 250
        enemy_hp = 500
        inventory = ["Apple", "Apple", "Apple"]
    else:
        type_it("What the? Invalid Difficulty?")
        type_it("Not on my watch.")
        sleep(3)
        type_it("Error 5, please contact support if you believe this is a mistake.")
    type_it("Redirecting to Main Menu...")
    new_menu()
    
def tutorial():
    new_menu()
    wait_time = 0.5
    txt_speed = 0.05
    border()
    type_it("Welcome to the game new player!")
    print_s("My name is Tutor and I will help")
    type_it("you learn how to play!")
    type_it("(^U^)")
    sleep(1)
    border()
    print_s("To start this off, a fighting")
    print_s("game wouldn't be much if you")
    print_s("couldn't fight, which is why")
    print_s("you can type 'fight' or 'f' to")
    type_it("deal some damage to your foe.")
    border()
    print_s("After fighting for a while,")
    type_it("you will take some damage.")
    print_s("Fortunately there are two")
    type_it("ways to heal yourself!")
    print_s("At the beginning of every")
    print_s("fight you will start with 2")
    type_it("apples.")
    print_s("Eating one will increase your HP")
    type_it("by 30.")
    type_it("To eat one, type 'eat'.")
    sleep(1)
    border()
    print_s("When you 'fight', you build")
    type_it("confidence.")
    print_s("Confidence can be used to give")
    type_it("you an edge in battle.")
    sleep(1)
    border()
    print_s("Using 5 confidence, you can heal")
    type_it("yourself 40 HP!")
    type_it("Give or take.")
    type_it("Sorta.")
    type_it("Maybe.")
    type_it("(O_O)")
    sleep(1)
    border()
    type_it("Anyway...")
    print_s("If you use 10 confidence, you will")
    type_it("unleash a super strong attack!")
    print_s("However, when you use any of these")
    print_s("actions, your confidence will go")
    type_it("down a lot.")
    type_it("Including if you miss a super attack!")
    print_s("That's right, you can indeed miss a")
    type_it("super attack, so be careful!")
    print_s("To heal, type 'heal' and to unleash")
    print_s("the fury of a thousand stars, type")
    type_it("'destroy'.")
    sleep(1)
    border()
    print_s("Oh, and you can quit the game at any")
    type_it("time by typing 'quit' or 'q'.")
    sleep(1)
    border()
    print_s("As a matter of fact, you can type")
    print_s("the first letter of any action to")
    type_it("use it!")
    print_s("So you could type 'h' instead of")
    print_s("'heal' to heal, 'd' instead of")
    print_s("'destroy' to unleash your strong")
    type_it("attack, ect.")
    type_it("(>oI)")
    sleep(1)
    border()
    print_s("Whew, that was long-winded, sorry")
    type_it("about that.")
    type_it("(^o^)`")
    print_s("To give a recap, 'fight' deals damage")
    print_s("and builds confidence,")
    print_s("'eat' uses an apple to heal you,")
    print_s("'heal' uses 5 confidence to heal you,")
    print_s("and 'destroy' uses 10 confidence to")
    type_it("deal a lot of damage.")
    type_it("Understand?")
    border()
    user_input = input(">")
    border()
    type_it("Good! Now get ready to...")
    type_it("Fight!")
    wait_time = 0.4
    txt_speed = 0.04

def main_menu(user_input):
    global game_start
    while True:
        new_menu()
        if user_input.lower() == "play" or user_input.lower() == "p":
            new_menu()
            game_start = True
            break
        if user_input.lower() == "difficulty" or user_input.lower() == "d":
            global difficulty
            global user_hp
            global max_hp
            global enemy_hp
            print("===========================")
            type_it("         Difficulty        ")
            print_s("Select your difficulty by")
            print_s("typing it into the prompt.")
            print_s("Easy: An easier experience")
            print_s("for players that are new")
            type_it("to this game.")
            print_s("Normal: The original gameplay")
            print_s("difficulty that the creator")
            type_it("intended the game to have.")
            if hard_unlocked:
                print_s("Hard: For more experienced")
                print_s("players. This difficulty")
                print_s("requires a little skill, and")
                type_it("a lot of luck.")
            type_it("Current difficulty set to")
            type_it(str(difficulty))
            user_difficulty_input = input(">")
            if user_difficulty_input.lower() == "easy" or user_difficulty_input.lower() == "e":
                global inventory
                user_hp = 100
                max_hp = 100
                enemy_hp = 100
                inventory = ["Apple", "Apple"]
                difficulty = "Easy"
                type_it("Difficulty set to " + str(difficulty))
                type_it("Redirecting to Main Menu")
                wait()
                break
            if user_difficulty_input.lower() == "normal" or user_difficulty_input.lower() == "n":
                #global inventory
                user_hp = 100
                max_hp = 100
                enemy_hp = 200
                inventory = ["Apple", "Apple", "Apple"]
                difficulty = "Normal"
                type_it("Difficulty set to " + str(difficulty))
                type_it("Redirecting to Main Menu")
                wait()
                break
            if hard_unlocked:
                if user_difficulty_input.lower() == "hard" or user_difficulty_input.lower() == "h":
                    user_hp = 250
                    max_hp = 250
                    enemy_hp = 500
                    difficulty = "Hard"
                    type_it("Difficulty set to " + str(difficulty))
                    type_it("Redirecting to Main Menu...")
                    wait()
                    break
            new_menu()
        if user_input.lower() == "credit" or user_input.lower() == "c":
            print("===========================")
            type_it("          Credits          ")
            type_it("Game made by Austin LaMarche")
            type_it("With help from Veerien Pala")
            print_s("And thank you to Mr. Raser")
            type_it("for teaching me Python 3")
            type_it("And thank YOU for playing")
            print_s("(Press enter to return")
            print_s("to the main menu)")
            user_input = input(">")
            new_menu()
            break
        if user_input.lower() == "quit" or user_input.lower() == "q":
            print("===========================")
            print_s("If you wish to quit the game,") 
            print_s("simply click the red stop")
            print_s("button at the top of this")
            print_s("screen. (Press enter to")
            print_s("return to the main menu)")
            user_input = input(">")
            new_menu()
            break
        else:
            type_it("Unknown Command. Try Again.")
            new_menu()
            print("===========================")
            print("   Welcome to Fight! (1.2) ")
            print("")
            print("        [   Play   ]       ")
            print("")
            print("        [Difficulty]       ")
            print("")
            print("        [  Credit  ]       ")
            print("")
            print("        [   Quit   ]       ")
            print("")
            print("===========================")
            user_input = input(">")
            new_menu()

#The beginning of the game starts with this line of code below.
in_menu = True
new_menu()
print("Note: To select an option on")
print("the menu, type it in to the")
print("command prompt. Example: type")
print("in 'play' or 'p' to select the")
print("play option. Another Note: DO")
print("NOT TYPE WHEN THE PROGRAM IS")
print("TYPING! Thanks.")
while True:
    while in_menu:
        if game_start:
            break
        print("===========================")
        print("   Welcome to Fight! (1.2) ")
        print("")
        print("        [   Play   ]       ")
        print("")
        print("        [Difficulty]       ")
        print("")
        print("        [  Credit  ]       ")
        print("")
        print("        [   Quit   ]       ")
        print("")
        print("===========================")
        user_input = input(">")
        main_menu(user_input)
    while True:
        type_it("Have you played Fight! before? (Y/N)")
        user_input = input(">")
        if user_input.lower == "yes" or user_input.lower() == "y":
            type_it("Then don't let me keep you,")
            type_it("Onward! To battle!")
            break
        elif user_input.lower() == "no" or user_input.lower() == "n":
            tutorial()
            break
        else:
            type_it("Sorry, I didn't understand that.")
            print("")
    new_menu()
    #Runs the game in a loop until a win or loss is detected.
    enemy_max = enemy_hp
    while not game_over:
        enemy_turn = False
        status()
        user_input = input(">")
        border()
        if user_input.lower() == "fight" or user_input.lower() == "f":
            user_attack()
            gain_confidence()
            if check_win(user_hp, enemy_hp):
                break
            enemy_turn = True
        elif user_input.lower() == "eat" or user_input.lower() == "e":
            eat()
            enemy_turn = True
        elif user_input.lower() == "heal" or user_input.lower() == "h":
            if confidence >= 5:
                heal()
                enemy_turn = True
            else:
                type_it("You need more confidence!")
        elif user_input.lower() == "destroy" or user_input.lower() == "d":
            if confidence >= 10:
                destroy()
                enemy_turn = True
            else:
                type_it("You need more confidence!")
        elif user_input.lower() == " " or user_input.lower() == "":
            type_it("Type your command next to the >")
        elif user_input.lower() == "quit" or user_input.lower() == "q":
            type_it("Are you sure you want to quit?")
            type_it("You will lose the fight! (Y/N)")
            user_input = input(">")
            if user_input.lower() == "yes" or user_input.lower() == "y":
                break
            else:
                type_it("Ok, let's continue")
        else:
            type_it("Invalid Command. Try Again.")
        if check_win(user_hp, enemy_hp):
            break
        if not enemy_turn:
            continue
        border()
        type_it("The enemy attacks!")
        enemy_attack()
        if check_win(user_hp, enemy_hp):
            break
        get_apple()
    
    #Checks is player won or lost and prints appropriate message in response.
    if check_win(user_hp, enemy_hp):
        border()
        type_it("You have vanquished your foe!")
        type_it("You Win!")
        border()
        voice("Good Job Hero.")
        voice("There will be many more fights") 
        voice("to come.")
        if difficulty == "Easy":
            border()
            print_s("Good Job! If you're looking for")
            print_s("more adventure, try Normal Mode")
            print_s("in the difficulty section of the")
            type_it("main menu.")
        if difficulty == "Normal":
            border()
            hard_unlocked = True
            print_s("Congratulations! You've unlocked")
            print_s("hard mode! You can change your")
            print_s("difficulty in the main menu and")
            type_it("continue your adventure!")
        border()
        voice("To be continued...")
        sleep(3)
    elif not check_win(user_hp, enemy_hp):
        border()
        type_it("You lost.")
        border()
        voice("Hero! Do not give up!")
        voice("This is not the end")
        voice("of your adventure.")
        voice("You can do it!")
        voice("Stay Confident!")
    border()
    undecisive = True
    while undecisive:
        if True:
            undecisive = False
            game_start = False
            game_over = False
            user_hp = 100
            enemy_hp = 200
            difficulty = "Normal"
            inventory = ["Apple", "Apple"]
            type_it("Difficulty set to Normal")
            type_it("Redirecting to Main Menu...")
            new_menu()
            continue
