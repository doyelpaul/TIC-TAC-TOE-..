
# TIC-TAC-TOE GAME
a=["_","_","_","_","_","_","_","_","_"]
def print_box():  
     print("|",a[0],"|",a[1],"|",a[2],"|")
     print("|",a[3],"|",a[4],"|",a[5],"|")
     print("|",a[6],"|",a[7],"|",a[8],"|")

players0 = input("Player 1 : ")
players1 = input("Player 2 :")
print(players0,"you will using X")
print(players1,"you will using 0")
def condition(s):
    c='X'
    d='0'
    if s[0]==s[1]==s[2]==c or s[0]==s[1]==s[2]==d:
        return True
    elif s[3]==s[4]==s[5]==c or s[3]==s[4]==s[5]==d:
        return True 
    elif  s[6]==s[7]==s[8]==c or s[6]==s[7]==s[8]==d:
        return True
    elif  s[0]==s[4]==s[8]==c or s[0]==s[4]==s[8]==d:
        return True
    elif  s[6]==s[4]==s[2]==c or s[6]==s[4]==s[2]==d:
        return True
    elif s[0]==s[3]==s[6]==c or s[0]==s[3]==s[6]==d:
        return True
    elif s[1]==s[4]==s[7]==c or s[1]==s[4]==s[7]==d:
        return True 
    elif s[2]==s[5]==s[8]==c or s[2]==s[5]==s[8]==d:
        return True 
    else :
         return False

def box(a):
    
    y=int(input("enter the position: "))
    if a[y-1]!='_':
        print("given position already taken , please choose new position")
        return box(a)
    else:
        return y
print_box()
for i in range(1,10):
    if i%2==0:
       print("turn of second player")
       x=box(a)
       a[x-1]='X'
       print_box()
       if condition(a):
            print("first player",players0,"won the game")
            break
    else:
        print("turn of frist player")
        x=box(a)
        a[x-1]='0'
        print_box()
        if condition(a):
            print("second player",players1,"won the game")
            break
        
print("game over")
        
         
         
        
    
        
    


    




