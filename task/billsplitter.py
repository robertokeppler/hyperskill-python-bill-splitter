# write your code here
import random

friends = {}
number_of_friends = int(input("Enter the number of friends joining (including you):\n"))
if number_of_friends > 0:
    print("Enter the name of every friend (including you), each on a new line:")
    for n in range(number_of_friends):
        friend = input()
        friends[friend] = 0
    print("Enter the total bill value:")
    total_bill = int(input())
    friends = dict.fromkeys(friends, round(total_bill / number_of_friends, 2))
    print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
    inp = input()
    if inp == "Yes":
        lucky_one = random.choice(list(friends.keys()))
        print(f"{lucky_one} is the lucky one!")
        for key, value in friends.items():
            if key == lucky_one:
                friends[key] = 0
            else:
                friends[key] = round(total_bill / (number_of_friends - 1), 2)
    elif inp == "No":
        print("No one is going to be lucky")
    print(friends)
else:
    print("No one is joining for the party")
