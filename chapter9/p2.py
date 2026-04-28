import random

def game():

    print("you are playing the game...")
    score=random.randint(1,44)

    with open("chapter9/hiscore.txt") as f:
        hiscore=f.read()
        if(hiscore!=""):
            hiscore=int(hiscore)
        else:
            hiscore=0

    print(f"your score is {score}")
    if(score>hiscore):
      
      with open("hiscore.txt","w") as f:
        f.write(str(score))
      return score
game()
