from more_functions import random_things as rt
import random


class NoSuchGamblingMethod(Exception):
    def __init__(self, message):
        self.message = str(message)
        print('NoSuchGamblingMethod:' + self.message)

# main function
methods = ['4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', 'big', 'small',
           'doubles', 'double 1', 'double 2', 'double 3', 'double 4', 'double 5', 'double 6',
           'triples', 'triple 1', 'triple 2', 'triple 3', 'triple 4', 'triple 5', 'triple 6']


def sicbo(choice, money):
    double = None
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    dice3 = random.randint(1, 6)
    value = dice1 + dice2 + dice3
    is_big = True if 11 <= value <= 18 else False  # Test if result is big or small
    triple = dice1 if dice1 == dice2 == dice3 else None  # Test if all 3 dices are the same
    if triple is not None:
        if dice1 == dice2 or dice1 == dice3:
            double = dice1
        elif dice2 == dice3:
            double = dice2
    else:
        double = None

    # Calculating result
    money_gain = 0
    if str(choice) == str(value):
        if value == 4 or value == 17:
            money_gain += money * 50
        elif value == 5 or value == 16:
            money_gain += money * 18
        elif (value == 6 and triple is not None) or value == 15:
            money_gain += money * 14
        elif value == 7 or value == 14:
            money_gain += money * 8
        elif (triple is None and (value == 9 or value == 12)) or value == 10 or value == 11:
            money_gain += money * 6
    elif ((choice == 'big' and is_big) or (choice == 'small' and not is_big)) and triple is None:
        money_gain += money * 2
    elif choice == 'doubles' and double is not None:
        money_gain += money * 6
    elif rt.split_string_into_list(choice, ' ')[0] == 'double' and \
            rt.split_string_into_list(choice, ' ')[1] == double:
        money_gain += money * 9
    elif choice == 'triples' and triple is not None:
        money_gain += money * 25
    elif rt.split_string_into_list(choice, ' ')[0] == 'triple' and \
            rt.split_string_into_list(choice, ' ')[1] == triple:
        money_gain += money * 15
    return money_gain, money, dice1, dice2, dice3


# Do 1 bet here by simply running this file
if __name__ == '__main__':
    print('Please enter the choice.')
    choice = input()
    if str(choice) not in methods:
        raise NoSuchGamblingMethod("There's no such method for you to gamble.")
    print('Please enter the money.')
    money = input()
    sicbo(choice, money)
