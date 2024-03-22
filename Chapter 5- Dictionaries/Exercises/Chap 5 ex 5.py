#making a list of dictionaries
pets = [
    {"animal": "cat",
     "owner":"rob"},
    {"animal": "goldfish",
     "owner":"rick"},
    {"animal":"dog",
     "owner":"mike"}
    ]
#printing
for pet in pets:
 print(f"Animal: {pet['animal']}")
 print(f"Owner: {pet['owner']}")
 
