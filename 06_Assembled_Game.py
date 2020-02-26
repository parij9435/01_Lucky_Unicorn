# End mechanics

import random

# functions go here


# main routine goes here

tokens = ["horse","horse","horse",
          "zebra", "zebra", "donkey",
          "donkey","donkey","donkey","unicorn"]

# assume start amount of $10
total = int(input("How ,much would you like to play with?"))

keep_going = ""
while keep_going == "":

    # choose a token from the list
    chosen = random.choice(tokens)


    # Adjust total correctly for a given token
    if chosen == "unicorn":
        total += 10
        feedback = "Congratulations, you got a unicorn.  You won $10.00"
    elif chosen == "donkey":
        total -= 1
        feedback = "Sorry you got a donkey, you did not win anything this round"
    else:
        total -= 0.5
        feedback = "You got a {}.  You paid a $1 and got back 50c".format(chosen)

    print()

    print(feedback)
    print("You have {:.2f} to play with".format(total))

    if total < 1:
        print("sorry you don't have enough money to continue. Game Over")
        keep_going = "end"
    else:
        keep_going = input( "Press <enter> to play again or any key to quit ")

print("Thank you for playing.")



    # Give user feedback
