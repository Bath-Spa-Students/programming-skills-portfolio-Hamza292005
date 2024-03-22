#making the loop
while True:
     age = input ("What is your age? ")
     if age == "quit":
         break
     age = int(age)
    #ages less than 3
     if age <3: 
         print("Your ticket is free")
         #ages 3-12
     elif age <=12:  
         print("Your ticket is 10$")  
     #for 13 and above
     else:
      print("Your ticket is 15$")    
      