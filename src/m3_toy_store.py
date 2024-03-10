###############################################################################
# DONE: 1. (3 pts)
#
#   In this module, we are going to create part of a program that could be used
#   by a toy store to keep track of prices of various toys.
#
#   For this _TODO_, write a function called get_toy() that simply prompts the
#   user for a toy like this:
#
#       "Please enter a toy: "
#
#   It should then return the toy as a string.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################

def get_toy():
    toy = input("Please enter a toy: ")
    return str(toy)

###############################################################################
# DONE: 2. (3 pts)
#
#   For this _TODO_, write a function called get_price() that simply prompts
#   the user for a price like this:
#
#       "Please enter a price: "
#
#   It should then return the price as a float.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################

def get_price():
    price = input("Please enter a price: ")
    return price

###############################################################################
# DONE: 3. (5 pts)
##
#   For this _TODO_, let's first create function called toy_price() that takes
#   2 parameters:
#       - toy       <-- str
#       - price     <-- float
#
#   This function should take the given toy and price and create a tuple where
#   the first element is the toy and the second one is the price. The toy
#   should be represented by a string and the price should be a float.
#
#   The function should return the tuple.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################

def toy_price(toy, price):
    toys = (toy, price)
    return toys

###############################################################################
# DONE: 4. (5 pts)
#
#   For this _TODO_, write a function called calculate_total_price() that takes
#   1 parameter:
#       toys    <-- list of tuples that contain toy (str) and price (float)
#
#   This function should take a list of tuples (like what you created in the
#   funciton above) and calculate the total cost of all the toys.
#
#   You will need to loop through each item, get the price for each one, and
#   total them as you go. Make sure you use the accumulator pattern here.
#
#   This function should return the total cost as a float.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################

def calculate_total_price(toys):
    total_cost = 0.0
    for price in toys:
        total_cost += price
    return float(total_cost)

###############################################################################
# TODO: 5. (8 pts)
#
#   For this _TODO_, write a function called main() that will start everything
#   off. Make sure you use the functions that you defined above where you can.
#
#   This function should have these criteria:
#
#       1. It should continually ask for information about toys.
#       2. It should first ask for the toy and then the price of that toy and
#          keep doing that until the user types "end" in either spot.
#       3. As it goes, is should create a tuple of this information and save
#          that tuple to a list.
#       4. If the user types "end" in either of the prompts it should not save
#          half of a tuple so you should NOT end up with a tuple that has a toy
#          but not a price.
#       5. Once you have all of the toys that the user entered, it should
#          calculate the total cost of all the toys.
#       6. It should then print each tuple on its own line
#       7. At the very end, it should print the total cost of all the toys like
#          this:
#
#           "Total Cost: $<COST HERE>"
#   
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################

def main():
    list_of_tuples = []
    tp = ()
    while True:
        toy = get_toy()
        if toy == "end":
            break
        list_for_tp = list(tp)
        list_for_tp.append(toy)
        tp = tuple(list_for_tp)
        price = get_price()
        if price == "end":
            list_for_tp = list(tp)
            list_for_tp.pop()
            tp = tuple(list_for_tp)
            break
        list_for_tp = list(tp)
        list_for_tp.append(price)
        tp = tuple(list_for_tp)
        list_of_tuples += tp
    total = calculate_total_price(list_of_tuples)
    for x in list_of_tuples:
        print(x)
    print(f"Total Cost: ${total}0")
main()