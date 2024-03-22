#defining a unction
def make_shirt(size,message):
    print(f"Size of the shirt is {size} and the message is {message}")
    
#callng the function using positional argument
make_shirt("large","Hey!") 

#calling the function using keyword argument
make_shirt(message="Hey!",size="Medium")   
