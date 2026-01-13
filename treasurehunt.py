print("welcome to Treasure island it is full of suspenses and adventure Here we go !!")
print ("Are you Ready?")
print ("Your mission is to find the treasure.")
choice1=input('you entered the game here comes a cross road , where you want to go ? Type "Left" or "Right".').lower()

if choice1=="right":
    choice2= input('There is a huge monster in the way sleeping gauarding the door,what will you do ?'
          'Type "fight" to fight the monster . type "hide" to hide and go from the monster' ).lower()
    if choice2 =="hide":
        choice4= input('you passed the gate hiding now you are at the island'
                       'there is house with two doors.'
                       'one"red", one "yellow".''choose one').lower()
        if choice4=="red":
            print("its a room full of fire GAME OVER ")
        else:   
            print("Congratulations you found the treasure filled with gold") 
        
    else:
        print("You cant fight the moster he is angry and way stronger than you so you die ..GAME OVER")   
else:
    choice3= input('There is a river in front of you ,it will help you to reach the island what will you choose?'
                   'Type "wait" to wait  for a boat . Type "swim" to swim across.').lower()
    if choice3=="wait":
        choice5 = input('you arrive at the island unharmed.'
                        'you see a house with two gates,'
                        'one "red" and one"Blue".'
                        'choose one ')
        if choice5=="red":
            print("OH no the room is filled with red hot lava you died !GAME OVER")
        else:
            print("Congratulations you found the mega treasure with golds and diamonds! YOU WIN")     
    
    


