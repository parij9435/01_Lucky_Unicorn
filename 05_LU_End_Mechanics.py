# End mechanics

import random

tokens = ["horse","horse","horse",
          "zebra", "zebra", "donkey",
          "donkey","donkey","donkey","unicorn"]

# assume start amount of $10
total = int(input("How ,much would you like to play with?"))

keep_going = ""
while keep_going == "":

    # allow manual token input for testing purposes
    chosen = input("enter a token: ")


    # Adjust total correctly for a given token
    if chosen == "unicorn":
        total += 10
        feedback = "Congratulations you won $10.00"
    elif chosen == "donkey":
        total -= 1
        feedback = "Sorry, you did not win anything this round"
    else:
        total -= 0.5
        feedback = "You paid a $1 and got back 50c"

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
