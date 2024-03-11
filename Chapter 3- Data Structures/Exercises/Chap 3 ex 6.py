# making a guest list

Guest_list = ["Abdur rahman","Abdullah","Waleed","Fahad"]

#Inviting each of them to dinner

print("dear " + Guest_list[0] + ", I would like to inform you that you're invited to my dinner tommorow")

print("dear " + Guest_list[1] + ", I would like to inform you that you're invited to my dinner tommorow")

print("dear " + Guest_list[2] + ", I would like to inform you that you're invited to my dinner tommorow")

print("dear " + Guest_list[3] + ", I would like to inform you that you're invited to my dinner tommorow")

#Printing the name of guest who isnt coming

print("It seems " + Guest_list[0] + " will not make it to dinner")

#Updating the list

Guest_list = ["Faiz","Abdullah","Waleed","Fahad"]

#Printing invitations again

print("dear " + Guest_list[0] + ", I would like to inform you that you're invited to my dinner tommorow")

print("dear " + Guest_list[1] + ", I would like to inform you that you're invited to my dinner tommorow")

print("dear " + Guest_list[2] + ", I would like to inform you that you're invited to my dinner tommorow")

print("dear " + Guest_list[3] + ", I would like to inform you that you're invited to my dinner tommorow")

#adding a line saying only 2 people can join

print("I'm sorry, it looks like I only have space for two people")

#Removing 2 people so only 2 remain

removed_guest = Guest_list.pop(0)

print("Sorry, " + removed_guest + ", I can't invite you to dinner")

removed_guest = Guest_list.pop(1)

print("Sorry, " + removed_guest + ", I can't invite you to dinner")

#Printing the message to invite remaining people

print(Guest_list[0] + ", you're invited to the dinner")

print(Guest_list[1] + ", you're invited to the dinner")

#Deleting the entire list

del Guest_list

print(Guest_list)