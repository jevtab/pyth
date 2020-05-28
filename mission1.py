#Defining three variables
interface = ('GigabitEthernet1/0/1')
status = ('up')
VLAN = 30
choice = ''
#Printing the initial information and asking for choice
print('\n***********************************')
print('\nThe interface', interface, 'has status', status, 'and VLAN', VLAN)
print('\n***********************************')
#Starting a loop that runs until the user enters the value for 'quit'.
while choice != 'q':
    # Give all the choices in a series of print statements.
    print('\n[1] Enter 1 to change status of the interface.')
    print('[2] Enter 2 to change VLAN.')
    print('[q] Enter q to quit.')

    # Ask for the user's choice.
    choice = input('\nWhat would you like to do? ')

    # Respond to the user's choice.
    if choice == '1' and status == 'up':
        status = ('down')
        print('\nInterface', interface, 'changed status to', status)
    elif choice == '1' and status == 'down':
        status = ('up')
        print('\nInterface', interface, 'changed status to', status)
    elif choice == '2':
        VLAN = input('Which VLAN would you like to have? ')
        print('\nNow the interface', interface, 'has status', status, 'and VLAN', VLAN)
    elif choice == 'q':
        print('\nThank you for using the application!\n')
    else:
        print("\nI don't understand that choice, please choose 1 or 2.\n")
