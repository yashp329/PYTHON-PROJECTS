import random

#randNo = random.randint(1,3)
#print(randNo)
 
#  SNAKE WATER AND GUN  |||||OR|||||  ROCK PAPER AND SCISSOR

def gameWin(comp,you):
    # If two values are same,  declare a tie! 
    if comp == you:
        return None

    # Check for all possibilites when computer chose 's '   
    elif comp == 's':
        if you == 'w':
            return False
        elif you == 'g':
            return True

    # Check for all possibilities when computer chose 'w'       
    elif comp == 'w':
        if you == 's':
            return True
        elif you == 'g':
            return False

    # Check for all possibilities when computer chose 'g'         
    elif comp == 'g':
        if you == 'w':
            return True
        elif you == 's':
            return False






print("Comp Turn : Snake(s) Water(w) or Gun(g)?")
randNo =  random.randint(1,3)
if randNo == 1:
    comp = 's'
elif randNo == 2:
    comp = 'w' 
elif randNo == 3:
    comp = 'g'          

you = input("Your turn : Snake(s) Water(w) Gun(g)?")
a = gameWin(comp,you)

print(f"COMPUTER CHOSE : {comp}")
print(f"YOU  CHOSE : {you}")

if a == None:
    print("Game is tie")
elif a:
    print('YOU WON !!!!!!')
else:
    print('YOU LOSE !!!!!!')        
