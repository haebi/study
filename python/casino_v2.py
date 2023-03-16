from random import randint

num_com = randint(0, 15)
# print(f"[DEBUG] com_num: {num_com}")

chance = 3
while (chance):
    num_user = int(
        input(f"Guess Computer Number [0-15] / {chance} chances left :"))

    if num_user < num_com:
        print(f"computer number is more than: {num_user}")
    elif num_user > num_com:
        print(f"computer number is less than: {num_user}")
    else:
        print(f"You Win!! com: {num_com} / you: {num_user}")
        break

    chance -= 1

    if chance == 0:
        print(f"The computer num is: {num_com}")
        print("You Lose")
