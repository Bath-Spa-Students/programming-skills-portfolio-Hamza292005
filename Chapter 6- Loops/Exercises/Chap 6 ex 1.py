#Making a loop
while True:
    topping = input("Enter your pizza topping(enter 'quit' to finish):")
    #breaking the loop
    if topping == "quit":
        break
    #printing the statement
    else:
     print("adding", topping, "to your pizza")