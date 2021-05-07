phonebook_database = {
    'otis': '678-458-2121'
}

print("""Electronic Phone Book
=====================
1. Look up an entry
2. Set an entry
3. Delete an entry
4. List all entries
5. Quit""")
select_number = int(input("What do you want to do (1-5)? "))
running = True
while running == True:
# Need to figure out how to get the while loop to return to the initial user_input prompt
    if select_number == 1:
        user_name = input("Name? ")
        print(user_name + "'s phone number is: " + phonebook_database[user_name])
        
    elif select_number == 2:
        user_name = input("Name? ")
        add_number = input("What is " + user_name + "'s phone number? ")
        phonebook_database[user_name] = add_number
        print("Entry stored for " + user_name)
    elif select_number == 3:
        user_name = input("Who would you like to delete? ")
        del phonebook_database[user_name]
        print(user_name + "has been removed.")
    elif select_number == 4:
        print("All current entries:\n" + str(phonebook_database))
    elif select_number == 5:
        print('See you next time!')
        running = False
    else:
        print(str(select_number) + " is not 1, 2, 3, 4, or 5!")