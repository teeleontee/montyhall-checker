from random import randint
from decimal import Decimal

counter_1_win = Decimal(0)
counter_2_win = Decimal(0)
counter_1_lost = Decimal(0)
counter_2_lost = Decimal(0)
print('How many doors do you want')
n = int(input())
# in the original there were 3 doors
def main():
    global counter_1_win
    global counter_2_win
    global counter_1_lost
    global counter_2_lost
    
    # in the original there were 3 doors

    choice1 = randint(1, n)  # your first pick

    car = randint(1, n)  # behind this door there's a car :)

    choice2 = randint(0, 1)  # choice2 is the choice to change doors
    # 1 is change
    # 0 is to stick with your original choice

    if choice1 == car and choice2 == 1:
        counter_2_lost += 1
    elif choice1 == car and choice2 == 0:
        counter_1_win += 1
    elif choice1 != car and choice2 == 1:
        counter_2_win += 1
    elif choice1 != car and choice2 == 0:
        counter_1_lost += 1


if __name__ == '__main__':
    for i in range(100000):  # how many tests we want to run
        main()  # the more tests we run, the more accurate the result will be
    print("if you don't change", counter_1_win / (counter_1_win + counter_1_lost))
    print("if you change      ", counter_2_win / (counter_2_win + counter_2_lost))
    counter_1_win = 0
    counter_2_win = 0
    counter_1_lost = 0
    counter_2_lost = 0
