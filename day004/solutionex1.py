def list_display_members(members):
    if not members:
        print("The members list is currently empty.")
    else:
        print("Members list:", members)

def list_add_element(members):
    element = input("Enter the name to add to the list: ")
    members.append(element)
    print(f"'{element}' has been added to the list.")

def list_add_elements(members):
    elements = input("Enter names to add (comma-separated): ")
    new_members = [name.strip() for name in elements.split(',')]
    members.extend(new_members)
    print(f"Elements {new_members} have been added to the list.")

def list_remove_element(members):
    try:
        index = int(input("Enter the index of the member to remove: "))
        if 0 <= index < len(members):
            removed_member = members.pop(index)
            print(f"'{removed_member}' has been removed from the list.")
        else:
            print("Invalid index! No member removed.")
    except ValueError:
        print("Invalid input! Please enter a valid index.")

def remove_last_element(members):
    if members:
        removed_member = members.pop()
        print(f"'{removed_member}' has been removed from the list.")
    else:
        print("The list is empty. No member to remove.")

def display_3_4_5_element(members):
    if len(members) < 5:
        print("Not enough members to display elements 3, 4, and 5.")
    else:
        print("Third member:", members[2])
        print("Fourth member:", members[3])
        print("Fifth member:", members[4])

def my_list_store():
    print("\nWelcome to Our List Store!!!")
    members_input = input("Please enter a comma-separated list of names: ")
    members = [name.strip() for name in members_input.split(',')]
    
    while True:
        print("\n*************** Menu **********************")
        print("Operations supported by our program are:")
        print("1: Display all elements in the members list")
        print("2: Add an element to the members collection")
        print("3: Add multiple elements to the members collection")
        print("4: Remove a member from the collection at a given index")
        print("5: Remove the last member from the collection")
        print("6: Display the third, fourth, and fifth element from the collection")
        print("7: Exit the Program")
        
        try:
            choice = int(input("Please enter your choice: "))
            if choice == 1:
                list_display_members(members)
            elif choice == 2:
                list_add_element(members)
            elif choice == 3:
                list_add_elements(members)
            elif choice == 4:
                list_remove_element(members)
            elif choice == 5:
                remove_last_element(members)
            elif choice == 6:
                display_3_4_5_element(members)
            elif choice == 7:
                print("Exiting the program. Goodbye!")
                break
            else:
                print("Invalid input, please try again!")
        except ValueError:
            print("Invalid input, please enter a number.")

# Run the program
my_list_store()
