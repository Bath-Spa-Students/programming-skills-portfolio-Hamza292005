#making a dictionary containing major rivers and countries they run through
rivers = {
    "Nile" : "Egypt",
    "Eupharates" : "Iraq",
    "Indus" : "Pakistan"
} 

#printing the values
for river, country in rivers.items():
    print(f"The {river} runs through {country}.")
for river in rivers.keys():
    print(river)
for country in rivers.values():
    print(country)    
        