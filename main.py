import random

r = random.randint(-1,1)   # To generate a random number between -1 , 1
'''
stone -1
paper 0
scissor 1
'''
print("Enter s for stone, p for paper and c for scissor")

choice = input("Enter your choice : ")

yourdict = {"s":"stone", "p":"paper", "c":"scissor"}
computerdict = {-1:"stone",0:"paper",1:"scissor"}
logicdict = {'s':-1,'p':0,'c':1}
you = logicdict[choice]

print(f"Computer choice : {computerdict.get(r)}")
print(f"Your choice : {yourdict.get(choice)}")

if r == logicdict.get(choice):
    print("Draw")
elif r-you == -1 or r-you == 2:
    print("You Won!")
elif r-you == -2 or r-you ==1:
    print("You Loss")
else:
    print("Something went wrong Contact Author")

'''
elif r==-1 and  you ==0: #-1
    print("You Won")
elif r==-1 and you == 1: #-2
    print("You loss")
elif r==0 and you == -1: #1
    print("you loss")
elif r==0 and you == 1: #-1
    print("you win")
elif r==1 and you == 0: #1
    print("you loss")
elif r==1 and you ==-1: #2
    print("You win")
'''




