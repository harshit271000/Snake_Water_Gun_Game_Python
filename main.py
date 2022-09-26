import random

def gameWin(comp, you):
    if comp == you:
        return None
    elif comp== 's':
        if you== 'w':
            return False
        elif you== 'g':
            return True    
    elif comp== 'w':
        if you== 'g':
            return False
        elif you== 's':
            return True    
    elif comp== 'g':
        if you== 's':
            return False
        elif you== 'w':
            return True    

randNo= random.randint(1,3)  # choose from 1 to 3 randomly

print("Computer Turn- Snake(s), Water(w) and Gun(g) ?")

if randNo == 1:
    comp= 's'
elif randNo == 2:
    comp= 'w'    
else:
    comp= 'g'    
    
you= input("Your Turn-  Snake(s), Water(w) and Gun(g) ?")

a= gameWin(comp,you)
print(f'Computer Chose- {comp}')
print(f'You Chose- {you}')

if a == None:
    print('Game is Tie')
elif a == True:
    print('You Win')
else:
    print('Computer Win')        