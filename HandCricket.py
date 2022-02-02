import random
from time import sleep
#1 means batting and 0 means bowling
class Computer:
    def __init__(self,run,wicket,over):
        self.score=run
        self.wicket=wicket
        self.over=over
    def run(self):
        return random.randint(1,6)
    def choice(self):
        return random.choice([0,1])

class Human:
    def __init__(self,run,wicket,over):
        self.score=run
        self.wicket=wicket
        self.over=over
    def toss(self):
        return random.randint(0,1)
    def run(self):
        x=int(input("Enter the run:"))
        if x>6:
            print("As you entered run >6, 1 will be deducted")
            return -1
        else:
            return x
    def choice(self):
        print("_____choice______")
        print("1 for batting")
        print("0 for bowling")
        ch=int(input("Enter your choice:"))
        return ch
def game(obj1,obj2):
    bowl=0
    print("Match is starting in..")
    for i in range(0,6):
        print("  ",5-i,"  ")
        sleep(1)
    while obj1.wicket>0 and obj2.over>0:
        bowl=bowl+1
        run1=obj1.run()
        run2=obj2.run()
        if run1==run2:
            print("It is Out")
            obj1.wicket=obj1.wicket-1
            print("Score is:{}/{}".format(obj1.score,obj1.wicket))
        else:
            obj1.score=obj1.score+run1

        if bowl==6:
            obj2.over=obj2.over-1
            bowl=0
            print("Remaing overs are:",obj2.over)
            print("Run is:",obj1.score)

    print("Final run is:",obj1.score)
    print("Over remaining",obj2.over)
         
if __name__ == '__main__':
    print("-1 run will be deducted, if you type run >6 run during your batting")

    over=int(input("For how many over will you want to play:"))
    wicket=int(input("For how many wicket will you want to play:"))

    player=Human(0,wicket,over)
    comp=Computer(0,wicket,over)
    print("For head print 0")
    print("For tail print 1")
    if player.toss()==int(input("Enter your choice:")):
        print("You have won the toss")
        playerChoice=player.choice()
        if playerChoice==1:
            print("You are going to bat")
            game(player,comp)
            print("You are going to bowl")
            game(comp,player)

            if player.score > comp.score:
                print("You win")
            else:
                print("Oops!Batter luck next time")
        else:
            print("You are going to bowl")
            game(comp,player)
            print("You are going to bat")
            game(player,comp)                      
            if player.score > comp.score:
                print("You win")
            else:
                print("Oops!Batter luck next time")

    else:
        print("You loss the toss")
        comChoice=comp.choice()
        if comChoice==0:
            print("You are going to bowl")
            game(comp,player)
            print("You are going to bat")
            game(player,comp)                      
            if player.score > comp.score:
                print("You win")
            else:
                print("Oops!Batter luck next time")
        else:
            print("You are going to bat")
            game(player,comp)
            print("You are going to bowl")
            game(comp,player)

            if player.score > comp.score:
                print("You win")
            else:
                print("Oops!Batter luck next time")
