import random
import celebs

celebs=celebs.celebs

first_celeb = random.choice(list(celebs.keys()))

score=0
game_on=True

while game_on:
    if score!=0:
        first_celeb = second_celeb

    second_celeb = random.choice(list(celebs.keys()))

    while True:
        if first_celeb == second_celeb:
            second_celeb = random.choice(list(celebs.keys()))
        else:
            break

    print("Compare A:", first_celeb)
    print("---------VS--------")
    print("Compare B:", second_celeb)

    choice=input("Who has more followers (A,B) : ")
    if choice.upper()=="A":
        if celebs.get(first_celeb)>celebs.get(second_celeb):
            print("Correct! You got 1 point")
            print()
            print("------------------------------------------------------------")
            print()
            score+=1
        else:
            print()
            print("Wrong! You lost the game!")
            print("Your score is",score)
            game_on=False
    elif choice.upper()=="B":
        if celebs.get(first_celeb) < celebs.get(second_celeb):
            print("Correct! You got 1 point")
            print()
            print("------------------------------------------------------------")
            print()
            score+=1
        else:
            print()
            print("Wrong! You lost the game!")
            print("Your score is",score)
            game_on=False

