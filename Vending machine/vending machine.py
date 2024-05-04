#Creating a vending machine
#intro
print("HELLO")
print("--------------------------------------------")
print("THIS IS A VENDING MACHINE\n")
print("PLEASE MAKE YOUR SELECTION")
#Data of all the items in the shop
items= {
    "0001":{"itemname":"Mars","itemprice":5,"stock":20},
    "0002":{"itemname":"Bounty","itemprice":4, "stock":30},
    "0003":{"itemname":"Break","itemprice":3, "stock":0},
    "0004":{"itemname":"kitkat", "itemprice":4, "stock":50},
    "0005":{"itemname":"Maltesers","itemprice":4,"stock":24},
    "0006":{"itemname":"toblerone","itemprice":10,"stock":26},
    "0007":{"itemname":"Sprite", "itemprice":3, "stock":12},
    "0008":{"itemname":"Lemon juice","itemprice":5,"stock":7},
    "0009":{"itemname":"Mirinda", "itemprice":3, "stock": 50},
    "0010":{"itemname":"Monster", "itemprice":6,"stock": 30},
    "0011":{"itemname":"Pepsi","itemprice":3,"stock": 40},
    "0012":{"itemname":"Pocari", "itemprice":5, "stock": 34},
    "0013":{"itemname":"Water","itemprice":2,"stock": 5},
    "0014":{"itemname":"Lays","itemprice":3,"stock": 20},
    "0015":{"itemname":"Oman chips","itemprice":2,"stock": 2}
}
# DEFINING A FUCTION TO DISPLAY THE MENU
def show_menu(items):
    print ("menu:")
    for code, item in items.items():
        print(f"code: {code} | {item['itemname']}: AED{item['itemprice']}: | Stock: {item['stock']}")
        
#  DEFINING A FUNCTION  FOR SELECTING AN ITEM AND CHECKIING FOR AVAILABILITY
def item_selection (items):
    while True:
        choice = input("What item would you like to purchase? enter its code: ")
        if choice in items and items[choice]["stock"] > 0: 
            return choice
        elif choice in items and items[choice]["stock"] == 0:
            print("This item is not avalaible sorry for inconvienience, please select another item")
        else:
            print("Incorrect code. Please try again.")

# DEFINING A FUNCTION THAT TAKES PAYMENT AND RETURNS CHANGE
def payment_process(item,price):
    while True:
        try:
            payment = float(input("Insert the money: AED"))
            if payment>= price:
                change = payment - price
                print(f"Thank you for the purchase! Here is your change:AED {change}")
                items[item]["stock"]-=1
                return
            else:
             print("Insufficient amount. please insert more money")
        except ValueError: 
           print("Please enter a valid amount")
           
# defining Main function
def vending_machine():
    show_menu(items)
    item = item_selection(items)
    price = items[item]["itemprice"]
    print(f'Your selection is {item}  price:AED {price}')
    payment_process(item,price)
    print(f"omitting {item} Thank you for using this machine")

# RUNNING THE VENDING MACHINE
vending_machine()    
       
              
            
            
        


