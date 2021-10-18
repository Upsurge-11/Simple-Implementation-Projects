import random

print("You have to guess the number which has been randomly generated between 1 and 1000.")
n = int(input("Enter the number of chances allowed :- "))
print("You have to achieve this feat within "+str(n)+" chances.")

key = random.randint(1, 1000)

check = False

for i in range(0, n):
    x = int(input("Enter your guess :- "))

    if x == key:
        check = True
        break
    elif x < key:
        print(str(x) + " is smaller than the key.")
    else:
        print(str(x) + " is larger than the key.")

if check:
    print("Congrats you won the game!!")
    print("The secret number was " + str(key) + ".")
else:
    print("Oops.. You lost the game!!")
    print("The secret number was " + str(key) + ".")
