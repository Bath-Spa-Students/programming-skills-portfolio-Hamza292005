#using the last ist and adding pastrami 3 times
sandwich_orders = ["Chicken","turkey","grilled cheese","pastrami","pastrami","pastrami"]
print("We have ran out of pastrami, apologies for any inconvinience")

#removing pastrami from sandwich orders
while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")
finished_sandwiches = []

#making rest of the sandwiches
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f" {current_sandwich.capitalize()} is done")
    finished_sandwiches.append(current_sandwich)
    
#printing finished sandwiches
print("finished sandwiches:") 
print(*finished_sandwiches, sep='\n')

 