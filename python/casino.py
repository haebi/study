from random import randint

num_com = randint(0, 15)
# print(f"[DEBUG] com_num: {num_com}")

Play = True
while (Play):
    num_user = int(input("Guess Computer Number [0-15]:"))

    if num_user < num_com:
        print(f"computer number is more than: {num_user}")
    elif num_user > num_com:
        print(f"computer number is less than: {num_user}")
    else:
        print(f"Correct!! com: {num_com} / you: {num_user}")
        Play = False
