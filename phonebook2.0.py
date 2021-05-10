def option_one():
    print("=====================")
    user_name = input("Name? ")
    if user_name in phonebook_database:
        print("=====================")
        print(user_name + "'s phone number is: " + phonebook_database[user_name])
        print("=====================")
    else:
        print("=====================")
        print(user_name + "'s phone number was not found.")
        print("=====================")
    user_response = input("Return to main menu? (y/n) ")
    if user_response == "y" or user_response == "yes":
        return
    else:
        print("=====================")
        print("See you next time!")
        quit()   
def option_two():
    print("=====================")
    user_name = input("Name? ")
    print("=====================")
    add_number = input("What is " + user_name + "'s phone number? ")
    phonebook_database[user_name] = add_number
    print("=====================")
    print("Entry stored for " + user_name + ".")
    print("=====================")
    user_response = input("Return to main menu? (y/n) ")
    if user_response == "y" or user_response == "yes":
        return
    else:
        print("=====================")
        print("See you next time!")
        quit()
def option_three():
    print("=====================")
    user_name = input("Who would you like to delete? ")
    del phonebook_database[user_name]
    print(user_name + " has been removed.")
    print("=====================")
    user_response = input("Return to main menu? (y/n) ")
    if user_response == "y" or user_response == "yes":
        return
    else:
        print("=====================")
        print("See you next time!")
        quit()
def option_four():
    print("=====================")
    print("All current entries:\n" + str(phonebook_database))
    print("=====================")
    user_response = input("Return to main menu? (y/n) ")
    if user_response == "y" or user_response == "yes":
        return
    else:
        print("=====================")
        print("See you next time!")
        quit()      
def option_five():
    print("=====================")
    print('See you next time!')
    quit()
def no_option():
    print(str(select_number) + " is not 1, 2, 3, 4, or 5!")
    print("=====================")
    user_response = input("Return to main menu? (y/n) ")
    if user_response == "y" or user_response == "yes":
        return
    else:
        print("=====================")
        print("See you next time!")
        quit()
phonebook_database = {
    'otis': '678-458-2121'
}
running = True
while running == True:
    print("""Electronic Phone Book
=====================
1. Look up an entry
2. Set an entry
3. Delete an entry
4. List all entries
5. Quit""")
    select_number = int(input("What do you want to do (1-5)? "))
    if select_number == 1:
        option_one()
    elif select_number == 2:
        option_two()     
    elif select_number == 3:
        option_three()
    elif select_number == 4:
        option_four()
    elif select_number == 5:
        option_five()
    else:
        no_option()