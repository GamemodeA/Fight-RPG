from time import sleep
import random

inventory = ["Apple", "Apple", "Apple"]
user_hp = 100         #Default value is 100
max_hp = user_hp      #Default value is user_hp
enemy_hp = 200        #Default value is 200
game_start = False    #Default value is False
game_over = False     #Default value is False
wait_time = 0.4       #Default value is 0.5
txt_speed = 0.04      #Default value is 0.05
difficulty = "Normal" #Default value is "Normal"
fast_mode = False     #Default value is False
stock = 0             #Default value is 0
tutorial_done = False #Default value is False
hard_unlocked = False #Default value is False
got_apple = False     #Default value is False

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
    for i in range(100):
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
def heal():
    global user_hp
    if user_hp < max_hp:
        try:
            inventory.pop()
            heal_num = random.randint(50, 60)
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
            heal()
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
        
def user_magic_attack():
    global enemy_hp
    global stock
    damage = random.choice("nnnnnnnmmnnnnnnnnmmnnnnnnnnmnmnnnnnnnmnmnnnnnnnncc")
    if stock == 1:
        damage_num = random.randint(10, 20)
    if stock == 2:
        damage_num = random.randint(20, 30)
    if stock == 3:
        damage_num = random.randint(40, 50)
    if stock == 4:
        damage_num = random.randint(70, 90)
    if stock == 5:
        damage_num = random.randint(100, 150)
    if damage == "n":
        enemy_hp -= damage_num
        type_it("Whabam! Your foe lost " + str(damage_num) + " HP!")
        stock = 0
        type_it("Your stock went back to 0")
    if damage == "m":
        type_it("Whif! Miss! Your foe lost no HP!")
        stock = 0
        type_it("Your stock went back to 0")
    if damage == "c":
        critical = random.randint(2, 3)
        total_damage = damage_num * critical
        if stock == 5:
            enemy_hp -= 999
            print_s("Magic out of control! Your foe")
            type_it("lost 999 HP!")
        else:
            enemy_hp -= total_damage
            print_s("Magic out of control! Your foe")
            type_it("lost " + str(total_damage) + " HP!")
        
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
    border()
    print("Your Health: " + str(user_hp))
    wait()
    print("Enemy Health: " + str(enemy_hp))
    wait()
    print("Inventory: " + str(inventory))
    wait()
    if stock >= 1:
        print("Magic Power: " + str(stock) + "X")
        wait()

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

def magic_tutorial():
    border()
    type_it("Wait one second!")
    print_s("I have something important") 
    type_it("to tell you!")
    print_s("There is actually more to")
    print_s("this fight than just fighting")
    type_it("and healing.")
    print_s("Now, you know that 'fight'")
    print_s("deals damage to the enemy,")
    type_it("and 'heal' gives you more health.")
    print_s("However, there are two more")
    type_it("actions you can do.")
    type_it("One of them is 'store'.")
    print_s("By typing 'store' or 's', you")
    type_it("can sacrifice a turn.")
    print_s("Now, why would you sacrifice a")
    type_it("turn?")
    print_s("Well, that's where the magic")
    type_it("attack comes in.")
    print_s("Depending on how many turns you")
    print_s("sacrifice, your magic attack will")
    print_s("do more damage. To unleash your")
    type_it("magic attack, type 'magic' or 'm'.")
    print_s("However! Be Warned! Your attack")
    type_it("has a small chance of missing!")
    print_s("And then all of those turns will")
    type_it("go to waste! So be smart about it.")
    type_it("I believe in you, hero.")

def main_menu(user_input):
    global game_start
    while True:
        if user_input.lower() == "play" or user_input.lower() == "p":
            new_menu()
            game_start = True
            break
        if user_input.lower() == "tutorial" or user_input.lower() == "t":
            print("===========================")
            type_it("          Tutorial         ")
            print_s("The goal of the game is to")
            print_s("beat the enemy. To do so,")
            print_s("type in 'f' or 'fight' to") 
            print_s("do some damage. If you want")
            print_s("to get some health back, type")
            print_s("'h' or 'heal' and you will")
            print_s("comsume one of the apples in")
            print_s("your inventory for some health.")
            print_s("If you want to quit the game,")
            print_s("type 'quit' or 'q' to exit")
            print_s("the game. Keep using these")
            print_s("commands and try to win!")
            print_s("Good Luck! (Press enter to")
            type_it("return to the main menu)")
            user_input = input(">")
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
        '''if user_input.lower() == "settings" or user_input.lower() == "s":
            global fast_mode
            print("===========================")
            type_it("         Settings          ")
            print_s("Type in a code into the")
            print_s("prompt, you get codes")
            type_it("throughout the game.")
            user_input = input(">")
            if user_input == "7474":
                if not fast_mode:
                    fast_mode = True
                    type_it("Fast Mode: On")
                else:
                    fast_mode = False
                    type_it("Fast Mode: Off")
                break
            #if user_input == "4747":'''
                
            
        
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
            break
        if user_input.lower() == "quit" or user_input.lower() == "q":
            print("===========================")
            print_s("If you wish to quit the game,") 
            print_s("simply click the red stop")
            print_s("button at the top of this")
            print_s("screen. (Press enter to")
            print_s("return to the main menu)")
            user_input = input(">")
            break
        else:
            type_it("Unknown Command. Try Again.")
            print("===========================")
            print("     Welcome to Fight!     ")
            print("[-----------Play----------]")
            print("[---------Tutorial--------]")
            print("[--------Difficulty-------]")
            #print("[---------Settings--------]")
            print("[----------Credit---------]")
            print("[-----------Quit----------]")
            print("===========================")
            user_input = input(">")

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
        print("     Welcome to Fight!     ")
        print("[-----------Play----------]")
        print("[---------Tutorial--------]")
        print("[--------Difficulty-------]")
        #print("[---------Settings--------]")
        print("[----------Credit---------]")
        print("[-----------Quit----------]")
        print("===========================")
        user_input = input(">")
        main_menu(user_input)
    #Runs the game in a loop until a win or loss is detected.
    while not game_over:
        if not tutorial_done and (enemy_hp <= 450 and enemy_hp >= 400):
            magic_tutorial()
            tutorial_done = True
        enemy_turn = False
        status()
        user_input = input(">")
        if user_input.lower() == "fight" or user_input.lower() == "f":
            user_attack()
            if check_win(user_hp, enemy_hp):
                break
            enemy_turn = True
        elif user_input.lower() == "heal" or user_input.lower() == "h":
            heal()
            enemy_turn = True
        elif user_input.lower() == " " or user_input.lower() == "":
            type_it("Type your command next to the >")
        elif user_input.lower() == "store" or user_input.lower() == "s":
            if stock < 5:
                stock += 1
                type_it("You now have " + str(stock) + " MP")
                enemy_turn = True
            else:
                type_it("You cannot stock up more than 5!")
        elif user_input.lower() == "magic" or user_input.lower() == "m":
            if stock > 0:
                user_magic_attack()
                enemy_turn = True
                if check_win(user_hp, enemy_hp):
                    break
            else:
                type_it("You have to store turns first!")
        elif user_input.lower() == "quit" or user_input.lower() == "q":
            type_it("Are you sure you want to quit? (Y/N)")
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
        voice("Stay Determined.")
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
            inventory = ["Apple", "Apple", "Apple"]
            type_it("Difficulty set to Normal")
            type_it("Redirecting to Main Menu...")
            new_menu()
            continue