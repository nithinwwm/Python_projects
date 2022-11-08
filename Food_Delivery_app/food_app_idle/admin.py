admin_keys = {'aadmin':'12345'}

Menu = {1:{'FoodID':1, 'Name':'Tandoori Chicken', 'Quantity':1, 'Price':240, 'Discount': '20%', 'Stock':'4pieces'},
        2:{'FoodID':2, 'Name':'Vegan Burger', 'Quantity':1, 'Price': 320, 'Discount':'10%', 'Stock':'3pieces'},
        3:{'FoodID':3, 'Name':'Truffle Cake', 'Quantity':500, 'Price': 900, 'Discount':'10%', 'Stock':'3500gm'}}


def add_food_item():
    foodID = int(input('Enter the FoodId : '))
    foodname = input('Enter the New Food Item to add : ' )
    quantity = int(input('Enter the quantity : ' ))
    price = int(input('Enter the price/piece : ' ))
    discount = input('Enter the discount you want to offer : ' )
    stock = input('Enter available stock of item : ' )
    Menu[foodID] = {'FoodID':foodID, 'Name':foodname, 'Quantity':quantity, 'Price':price, 'Discount':discount, 'Stock':stock}
    
    print(f'The item {foodname} has successfully added to the Menu')
    return Menu
    
def edit_food_item():
    print(Menu)
    item = int(input('Enter the foodId you wish to edit : '))
    a = input('Enter the Food item, edited name : ')
    b = int(input('Enter the new price : '))
    c = input('Enter the new available Stock : ')
    Menu[item]['Name'] = a
    Menu[item]['Price'] = b
    Menu[item]['Stock'] = c
    print('********** Food Item edited successfully **********')
    return Menu

def view_menu():
    print('********** Available Food Items in the Menu **********')
    for i in Menu:
        print('Item ID : ',Menu[i]['FoodID'])
        print('Item Name : ',Menu[i]['Name'])
        print('Item Price : ',Menu[i]['Price'], 'INR')
        print('Stock Available : ',Menu[i]['Stock'])
        
def remove_item():
    d = int(input('Enter the foodID you wish to remove : '))
    Menu.pop(d)
    print('********** Item Removed Successfully **********')
    return Menu
