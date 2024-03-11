#storing places to visit
places = ["Damascus","Cairo","Baghdad","Cordoba"]

#Printing the list in original order
print("Original order:", places)

#Printing the list in alphabetical order
print("Alphabetical order:", sorted(places))

#Printing in original order
print("Original order:", places)

#Printing in reversed alphabetical order
print("Reversed Alphabetical order:", sorted(places, reverse=True))

#Printing in original order
print("Original order:", places)

#Changing the order using reversed
places.reverse()

#Showing order has been reversed
print("Reversed order:", places)

#Changing the order of the list again using reverse and printing
places.reverse()
print("Original order:", places)

#list in alphabetical order using sort()
places.sort()
print("sorted list:", places)

#list in reverse alphabetcal using sort
places.sort(reverse=True)
print("list in reverse alpahabetical using sort():", places )
