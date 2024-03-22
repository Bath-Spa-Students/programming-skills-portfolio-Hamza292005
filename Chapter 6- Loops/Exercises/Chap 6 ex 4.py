#making a list caleed sandwich_orders
sandwich_orders = ["Chicken","turkey","grilled cheese"]
#empty list of finished sandwiches
finished_sandwiches = []
#starting loop
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I made your {current_sandwich.capitalize()} sandwich")
    finished_sandwiches.append(current_sandwich)
    
#printing the finished list
print(f"finished sandwiches :") 
print(*finished_sandwiches, sep='\n')   
