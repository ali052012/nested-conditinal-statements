
print("Select your ride: ") 
print("1. Bike")
print("2. Car")

#take input of number 1 or 2
#select your ride
choice = int(input("Enter your choice: ") )

#User entering option 1
if(choice == 1): #condition 1 outer if statement
    print("what type of bike?")
    print("1.Scooty\n")
    print("2.Scooter\n")
#Condition for selecting the type of bike
    choice2 =int(input("Enter you choice2: "))
    if choice2==1: #inner if statement
       print("you have selected scooty")
    else:
       print("you have selected scooter")

#user entering option 2 
elif( choice == 2):  #outer elif statement
   print("what type of car")
   print("sedan")
   print("xuv")
   choice3=int(input("enter your choice3"))

   if choice3==1: #inner if statement
#condition for selecting the type of car
    print("you have selected sedan")

   else: #outer else statement
    print("you have selected xuv")

else:#outer else statement
    print("wrong choice")

 