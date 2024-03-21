from random import shuffle
my_list = ['', '0', '']


def shuffle_list(list_1):
    shuffle(list_1)
    return list_1


# shuffles main list
def get_inp():
    user = int(input("mimic the position: "))
    while user not in [0, 1, 2]:
        print("Invalid input. Please enter 0, 1, or 2.")
        user = int(input("mimic the position: "))

    return user



def check(list_1, user_guess):
    # while(user_guess != 0 or 1 or 2):
    if list_1[user_guess] == '0':
        print("Congrats! you won")
        print(list_1)
    else:
        print("You lost!")
        print(list_1)


# lets start


def main():
    while True:
        print(my_list)
        guess = get_inp()
        new_list = shuffle_list(my_list)
        check(new_list, guess)
        a = input("Do you wan to play again!?: (Y or N) ")
        if a not in ["Y","N"]:
            a = input("Invalid input, Do you wan to play again!?: (Y or Y)")
        if a == "Y":
            pass
        else:
            exit()

main()