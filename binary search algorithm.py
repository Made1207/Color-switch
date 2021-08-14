import random
import sys

#creates a list of 1000 random numbers from -3000 to 3000
def get_list():
    list1 = []
    length = 1000
    for i in range(1, length):
        list1.append(random.randint(-3000, 3000))
    for i in list1:
        if list1.count(i) > 1:
            list1.remove(i)
            list1.append(random.randint(-3000, 3000))
    binary_search(list1)

#performs binary searching through the list
def binary_search(list1):
    list1.sort()
    print(list1)
    print('Binary searching is a method of looking for an object in a list by checking if the object is in one half of the list and if it is not, removing that half from the list. It continues to do this until either the object in question is at the middle of the list or is the only item in the list.')
    print('This program searches for a number through a list through binary searching.')
    user_input = int(input('Enter the number you want to check: '))
    while len(list1) != 1:
        print(list1)
        middle = len(list1)//2
        print(len(list1))
        if list1[middle] == user_input:
            print(list1)
            print(len(list1))
            print('Your number is found')
            sys.exit()
        num_rem = len(list1) - middle
        if list1[middle] > user_input:
            for i in range(0, num_rem):
                list1.remove(list1[len(list1) - 1])
        elif list1[middle] < user_input:
            for i in range(0, num_rem):
                list1.remove(list1[0])
    else:
        if list1[0] == user_input:
            print(list1)
            print(len(list1))
            print('Your number is found')
        elif list1[0] != user_input:
            print(list1)
            print('This number is not in the list.')

get_list()