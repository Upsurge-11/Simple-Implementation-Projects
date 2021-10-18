import random

n = int(input("Enter the number of snakes/ladders required :- "))

elements = []

for i in range(0, n):
    start = random.randint(1, 100)
    end = random.randint(1, 100)
    elements.append([start, end])

occur = [0] * 101

snake_and_ladder = []

for i in elements:
    if occur[i[0]] == 0 and i[0] != 100 and i[0] != i[1]:
        snake_and_ladder.append(i)
    occur[i[0]] += 1

while len(snake_and_ladder) < n:
    start = random.randint(1, 100)
    end = random.randint(1, 100)
    if occur[start] == 0:
        snake_and_ladder.append([start, end])

snake_and_ladder.sort()

print("\n-------------------------------------------------------------------------------------\n")

print("The snakes and ladder positions are as follows :-")

for i in snake_and_ladder:
    if i[0] > i[1]:
        print("Snake at", i[0], "->", i[1])
    else:
        print("Ladder at", i[0], "->", i[1])

print("\n-------------------------------------------------------------------------------------\n")

a = b = 0

while True:
    input("Hit enter to roll the dice for player A.")
    dice_a = random.randint(1, 6)
    print("Player A got", dice_a)
    move_a = dice_a
    if dice_a < 6:
        move_a = dice_a
    else:
        move_a = dice_a
        while dice_a == 6:
            dice_a = random.randint(1, 6)
            print("Player A got", dice_a)
            move_a += dice_a
            if move_a >= 18:
                print("Player A got consecutive 3 6s.")
                move_a = 0
    a += move_a

    if a > 100:
        a -= move_a
    elif a == 100:
        print("\n-------------------------------------------------------------------------------------\n")
        print("Player A reached 100!!")
        print("PLayer A won.")
        print("\n-------------------------------------------------------------------------------------\n")
        break

    for i in snake_and_ladder:
        if a == i[0]:
            if a > i[1]:
                print("Oops.. PLayer A encountered a snake!")
                print(str(i[0])+"->"+str(i[1]))
            if a < i[1]:
                print("Congo.. PLayer A reached a Ladder!")
                print(str(i[0]) + "->" + str(i[1]))
            a = i[1]
            break

    print()
    print("PLayer A is in", a)
    print("\n-------------------------------------------------------------------------------------\n")

    input("Hit enter to roll the dice for player B.")
    dice_b = random.randint(1, 6)
    print("Player B got", dice_b)
    move_b = dice_b
    if dice_b < 6:
        move_a = dice_b
    else:
        move_b = dice_b
        while dice_b == 6:
            dice_b = random.randint(1, 6)
            print("Player B got", dice_b)
            move_b += dice_b
            if move_b >= 18:
                print("Player B got consecutive 3 6s.")
                move_b = 0
    b += move_b

    if b > 100:
        b -= move_b
    elif b == 100:
        print("\n-------------------------------------------------------------------------------------\n")
        print("Player B reached 100!!")
        print("PLayer B won.")
        print("\n-------------------------------------------------------------------------------------\n")
        break

    for i in snake_and_ladder:
        if b == i[0]:
            if b > i[1]:
                print("Oops.. PLayer B encountered a snake!")
                print(str(i[0]) + "->" + str(i[1]))
            if b < i[1]:
                print("Congo.. PLayer B reached a Ladder!")
                print(str(i[0]) + "->" + str(i[1]))
            b = i[1]
            break

    print()
    print("PLayer B is in", b)
    print("\n-------------------------------------------------------------------------------------\n")

print("Thank You for playing!!")
