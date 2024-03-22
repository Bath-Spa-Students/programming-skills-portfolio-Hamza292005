#defining the function with default size and message
def make_shirt(size="large", message="I love python"):
    print(f"Creating a shirt with size {size} and message {message}")
    
#calling the default function
make_shirt()   
 
#now with default message and different size
make_shirt(size="medium")

#now with default size and different message
make_shirt(message="I hate python")
 