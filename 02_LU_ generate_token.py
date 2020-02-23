# Lucky Unicorn Decomposition Step 2
# Generate a random token

# to do
# set up starting amount
# choose 100 tokens (ie: play 100 rounds and...
#   count # of unicorns and multiply by 5
#   count # of horse / zebra and multiply by 0.5
#   count # of donkeys
#   work out the total won / lost

import random

HOW_MUCH = 100
tokens = ["horse", "zebra", "donkey", "unicorn"]

unicorn_count = 0
zebhor_count = 0
donkey_count = 0

for item in range (1,HOW_MUCH):

    chosen = random.choice(tokens)

    if chosen == "unicorn":
        unicorn_count += 1
    elif chosen == "donkey":
        donkey_count += 1
    else:
        zebhor_count += 1

    print(chosen)

print ("**** Win / Loss Calculations****")
print("# Uncorns: {}".format(unicorn_count))
print("# Zebra / Horses: {}".format(zebhor_count))
