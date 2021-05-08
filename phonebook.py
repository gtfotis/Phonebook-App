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
        print("=====================")
        user_name = input("Name? ")
        print("=====================")
        print(user_name + "'s phone number is: " + phonebook_database[user_name])
        print("=====================")
        user_response = input("Return to main menu? (y/n) ")
        if user_response == "y" or user_response == "yes":
            continue
        else:
            print("=====================")
            print("See you next time!")
            running = False
    elif select_number == 2:
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
            continue
        else:
            print("=====================")
            print("See you next time!")
            running = False
            break        
    elif select_number == 3:
        print("=====================")
        user_name = input("Who would you like to delete? ")
        del phonebook_database[user_name]
        print(user_name + " has been removed.")
        print("=====================")
        user_response = input("Return to main menu? (y/n) ")
        if user_response == "y" or user_response == "yes":
            continue
        else:
            print("=====================")
            print("See you next time!")
            running = False        
    elif select_number == 4:
        print("=====================")
        print("All current entries:\n" + str(phonebook_database))
        print("=====================")
        user_response = input("Return to main menu? (y/n) ")
        if user_response == "y" or user_response == "yes":
            continue
        else:
            print("=====================")
            print("See you next time!")
            running = False       
    elif select_number == 5:
        print("=====================")
        print('See you next time!')
        running = False
    else:
        print(str(select_number) + " is not 1, 2, 3, 4, or 5!")
        print("=====================")
        user_response = input("Return to main menu? (y/n) ")
        if user_response == "y" or user_response == "yes":
            continue
        else:
            print("=====================")
            print("See you next time!")
            running = False