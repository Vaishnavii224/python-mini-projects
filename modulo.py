#number_to_check =int(input("What is the number you want to check"))
#if number_to_check % 2 == 0:
#   print("Even")
#else:
#   print("odd")  
print("Welcome to bright classes:)")
Grade = int(input("Which grade are you in ?"))
Fees = 100000

if Grade >=5:
    print("You are eliglible for your class to your bright future")
    grade = int(input("Enter your last semester score in percent out of 100"))
    if grade >=90:
        Fees = 25000
        print("congratulations! you get a discount of 75%")
    elif grade >=80:
        Fees = 50000
        print("congratulations!you get a discount of 50%")
    elif grade >=70:
        Fees = 75000
        print("Congratulations you get a discount of 25%")
    else:
        print("We are sorry we dont have any discount for you but a bright future.")
    Fee_waviver = input("Do you belong to the economically weaker section? Type y for yes and n for no.") 
    if Fee_waviver =="y":
       Fees -=5000 
    print(f"your total fees is Rs{Fees}")     
else:
    print("Sorry but we dont accept students under 5th grade. thanyou!")                    
        
    