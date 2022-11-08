import admin as aa
from user import User

print('********** WELCOME TO FOODZY **********')

uhh = User(str,str,str,str,str)
inp = int(input('\nPlease select an Option to Login \n1.ADMIN \n2.USER \n3.EXIT ' ))

if inp == 1:
    username = input('Enter the username of admin : ')
    password = input('Enter the admin password : ')
    if aa.admin_keys[username] == password:
        print('\n***** You are Successfully LoggedIn as aadmin *****')
        admin_crawler = True
        while admin_crawler:
            admin_choice = int(input('\nPlease select an option from Admin panel : \n1. Add New Food Item \n2. Edit Food Item \n3. View Menu \n4. Remove Item from Menu \n5. Exit'))
            if admin_choice == 1:
                aa.add_food_item()
            elif admin_choice == 2:
                aa.edit_food_item()
            elif admin_choice == 3:
                aa.view_menu()
            elif admin_choice == 4:
                aa.remove_item()
            elif admin_choice == 5:
                print('You have opted to exit out of admin panel')
                admin_crawler = False
            else:
                print('Please select a valid Input!!')
    else:
        print('!!!!! Username and Password doesnot Match !!!!!')
        
elif inp == 2:
    
    print('\n***** WELCOME to FOODZY *****')
    inp2 = int(input('\nPress 1 to Create a New account \nPress 2 to Login \nPress 3 to Exit '))
    if inp2 == 1:
        print(' Welcome to user register panel ')
        uhh.create_new_user()
    elif inp2 == 2:
        print('Welcome to User Login panel')
        username = input('Enter your username : ')
        password = input('Enter your password : ')
        if User.login(username,password):
            print(f'\n***** Login successful for {username} *****')
            user_crawler = True
            while user_crawler:
                usr_choice = int(input(f'{username}, Select an option \n1. Place New Order \n2. Order History \n3.Update Profile \n4.Exit '))
                if usr_choice == 1:
                    uhh.new_order()
                elif usr_choice == 2:
                    print(f'Here is your previous Order History , {username}')
                    print(uhh.order_history)
                elif usr_choice == 3:
                    pass
                elif usr_choice == 4:
                    print('***** You are Successfully Logged Out *****')
                    user_crawler = False
                else:
                    print('Please Select a Valid Option!!')
        else:
            print('!!!!! Try again !!!!!')
    else:
        exit()

else:
    exit()
