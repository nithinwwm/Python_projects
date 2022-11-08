import admin as ad

class User:

    #user_info = {}
    login_info = {'a':'67890'}
    
    def __init__(self, fullname, phoneno, email, address, password):
        self.fullname = fullname
        self.phoneno = phoneno
        self.email = email
        self.address = address
        self.password = password
        User.login_info[self.fullname] = self.password
        self.profile = {'Name' : fullname}
        self.order_history = {}
        
 
    def create_new_user(self):
        self.fullname = input('Enter your Fullname : ')
        self.phoneno = int(input('Enter your Phone Number : '))
        self.email = input('Enter your Email ID : ')
        self.address = input('Enter your Address : ')
        self.password = input('Enter your new Password : ')
        User.login_info[self.fullname] = {'UserName': self.fullname,
                                    'Phone No': self.phoneno,
                                    'Email ID': self.email,
                                    'Address' : self.address}
        print(f'\n***** User registration Successfull for \t{self.fullname}*****')
        
        
    @classmethod
    def login(cls,username,password):
        if cls.login_info.get(username) == password:
            print('..........You are successfully logged in..........')
            return True
        else:
            print('!!!!! Invalid Username or Password !!!!!')
            return False

    
    def new_order(self):
        print('Please select the items from the Menu')
        print(ad.view_menu())
        user_choice = int(input('If you want to place order Select 1.Yes or 2.No '))
        if user_choice == 1:
            
            n = int(input('Please enter the number of items you wish to place order : '))
            price = 0
            for i in range(n):
                foodID = int(input('Enter the foodId here: '))
                quant = int(input('Enter the quantity of item: '))
                price += ad.Menu[foodID]['Price'] * quant
                print(f'The price of your order is : {price} INR')
                
            ask_again = int(input('To confirm Press 1 \nTo cancel Press 2 '))
            if ask_again == 1:     
                print(f"The name of your food item is {ad.Menu[foodID]['Name']}")
                print(f"This is you quantity {quant}")
                print(f"It costs you {price} INR in total")
                print("You're all set for this Order")
                self.order_history[foodID] = {'Item Name': ad.Menu[foodID]['Name'],
                                              'Quantity': quant,
                                              'Item Price' : ad.Menu[foodID]['Price']}
                final_stock = (ad.Menu[foodID]['Stock'])-quant
                ad.Menu[foodID]['Stock'] = final_stock
                print('Order Placed Successfully')
            elif ask_again == 2:
                print(' Order has been Canceled')
            else:
                print('Invalid Choice')
        elif user_choice == 2:
            print('You have selected option 2, So we have cancelled this')
        else:
            print('Please enter Valid number')
                
