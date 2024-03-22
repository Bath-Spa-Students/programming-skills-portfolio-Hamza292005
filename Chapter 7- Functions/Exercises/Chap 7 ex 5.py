#defining a variable called describe city
def describe_city(city, country="UAE"):
    print(city,"is in "+ country)
    
#calling the function with correct cities
describe_city("dubai".capitalize())
describe_city("ajman".capitalize())

#calling the fuction with incorrect city
describe_city("riyadh".capitalize())
