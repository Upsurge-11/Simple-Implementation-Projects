import random

option = ["Rock","Paper","Scissors"]

print("1. Rock")
print("2. Paper")
print("3. Scissors")

check = True

while check:
    player = input()

    cpu = random.choice(option)

    if player == cpu:
        print("Tie!")
        print("CPU choosed "+cpu+" :)")
    elif (player == "Rock" and cpu == "Scissors") or (player == "Paper" and cpu == "Rock") or (player == "Scissors" and cpu == "Paper"):
        print("You win!")
        print("CPU choosed "+cpu)
    elif (cpu == "Rock" and player == "Scissors") or (cpu == "Paper" and player == "Rock") or (cpu == "Scissors" and player == "Paper"):
        print("You lose!")
        print("CPU choosed "+cpu)
    else:
        print("Invalid entry!")
        print("CPU choosed "+cpu)
    print("Do you want to play more?")
    print("Y = Yes and N = No")
    o = input()
    if o == "N":
        print("Thank You!! :)")
        check = False
    elif o == "Y":
        check == True
    else:
        print("Invalid entry!")
        break