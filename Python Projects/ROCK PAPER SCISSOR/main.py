import random
# ROCK PAPER AND SCISSOR !!!!!!!

def winGame(comp,you):
    if comp == you:
        return None
    elif comp == 'r':
        if you == 's':
            return False
        elif you == 'p':
            return True
    elif comp == 's':
        if you == 'p':
            return False
        elif you == 'r':
            return True                
    elif comp == 'p':
        if you == 's':
            return True
        elif you == 'r':
            return False




print("Comp Turn : Rock(r) Paper(p) and Scissor(s) ?")
randNO =  random.randint(1,3)
if randNO == 1:
    comp = 'r'
elif randNO == 2:
    comp = 'p'
elif randNO == 3:
    comp = 's'   


you = input("Your Turn : Rock(r) Paper(p) and Scissor(s) ?")    
a = winGame(comp,you)

print(f" COMPUTER CHOSE {comp}")
print(f" YOU CHOSE {you}")




if a == None:
    print("GAME IS A TIE !!!!!")
elif a:
    print("YOU WON  !!!!!!")   
else:
    print("YOU LOSE !!!!!!")     
