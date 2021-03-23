#Dice Simulator

import random


class Dice_Sim:
    def __init__(self):
        self.lst=[]
        self.count=0
        
    def Cust_Dice(self):
        dice=random.randint(1,6)
        #dice output will be saved in list
        self.lst.append(dice)
        #calling the count of 6
        self.count=self.lst.count(6)
        #check whether the count is odd then bring the 6 in game
        if self.count%2!=0:
            #appending another 6 to avoid 6 again and again
            self.lst.append(6)
            return(6)
        
        return dice
    
    
    def Dice(self):
        dice=random.randint(1,6)
        return dice    

def Player():
    d=Dice_Sim()
    #we asked user whether he wanna switch to the custom dice or not???
    choice=str(input("Do you want to switch the dice where no of occurence of 6 is great?? Y?N:"))
    user=str(input("Do you want to play Y/N:"))
    if choice =="N":    
        #took the input and keep in loop which asks user again and again if decision is N so terminate the game else keep running
        while user:
            if user == 'Y':
                print(d.Dice())
                user=str(input("Do you want to play Y/N:"))
            else:
                print('Closing')
                break
    else:
        while user:
            if user == 'Y':
                print(d.Cust_Dice())
                user=str(input("Do you want to play Y/N:"))
            else:
                print('Closing')
                break 



#-----Driver Code-----

#Player()

