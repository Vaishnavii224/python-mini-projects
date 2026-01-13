print("Welcome to learing code selling pizza!")
Size = input("what size pizza do you want ? S, M or L:")
Panner = input("Do you Want paneer in your Pizza?")
Extra_Cheese = input ("Do you want extra cheese ? Y or N :")

bill = 0
if Size== "S":
    bill+= 150 
elif Size== "M":
    bill+= 200
elif Size== "L":
    bill+=250
else:
    print("You entered wrong inputs.")
    
if Panner== "Y":
    if Size == "S":
        bill +=20
    else:
        bill +=30

if Extra_Cheese == "Y" :
    bill +=1
    
print(f"Your finall bill is :Rs{bill}.")  
        
        
                           