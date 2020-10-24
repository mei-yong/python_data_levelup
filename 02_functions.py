'''
Python Exercises 2 - Functions
Author: github.com/mei-yong
Date Updated: 2020-10-24
'''

###############################################################

# Example function - no inputs, no outputs
def print_hello():
    print("Hello")

print_hello()


# Example function - has inputs, no outputs
def print_greeting(your_name):
    print(f"Salutations {your_name}")

print_greeting("Mr Holmes")


# Example function - has inputs, no outputs - some inputs are optional
def print_fruit(fruit, num_fruit=5):
    str_plural = 's' if num_fruit > 1 else ''
    print(f"There are {num_fruit} {fruit}{str_plural}")

print_fruit('apple') # call on the function without providing the optional variable
print_fruit('apple', num_fruit=8) # call on the function and provide the optional variable
#print_fruit() # this will error because whilst num_fruit is optional, fruit is mandatory


# Example function - has inputs and outputs
def some_calc(input_num):
    return input_num * 2 + 5

# it is important that you assign the outputs of a function to a variable if you want to use it later
result_num = some_calc(2)
print(result_num)


# Example function - has 2 inputs and 3 outputs
def some_calc_multi(num_1, num_2):
    num_1_new = num_1 * 2
    num_2_new = num_2 + 5
    num_3 = num_1_new + num_2_new
    return num_1_new, num_2_new, num_3

a, b, c = some_calc_multi(2, 5)
print(a, b, c)

###############################################################

# The above is all well and good but you might be wondering what the point of functions are. Lemme explain with an example

# Here is one way to write code that adds 2 numbers and then multiplies them by 2
num_1 = 10
num_2 = 20
num_3 = (num_1 + num_2) * 2
num_4 = 3
num_5 = 5
num_6 = (num_4 + num_5) * 2
num_7 = 10
num_8 = 20
num_9 = (num_7 + num_8) * 2
print(num_3, num_6, num_9)

# Now what happens if circumstances change and now you also need to add 5 on top of the result?
num_1 = 10
num_2 = 20
num_3 = ((num_1 + num_2) * 2) + 5 # if you've got attention to detail, you could get this right
num_4 = 3
num_5 = 5
num_6 = (num_4 + num_5) * 2 + 5 # but you could very easily forget a bracket somewhere
num_7 = 10
num_8 = 20
num_9 = ((num_7 + num_8) * 2) + 8 # or have a typo and add 8 instead of 5
print(num_3, num_6, num_9)

# And this is a super simple example, what if this code was 80 lines long?
# Or if this calculation doesn't exist in just this one python file but also needs to be changed in lots of other files? (ok, the solution this requires something a little further than just functions (importing and packing python files) but we can cover that later - remind me)
# And that's the point of functions, to make repeatable tasks easier to read, edit, and execute


# This code below does the same thing as above but is much less of a pile of flaming dumpster spaghetti (note: it's not the most efficient code though - look up O notation for further reading)
# It also uses some tips & tricks to make code more readable which is super important if you don't want your other dev team mates to toss you into the Thames after reviewing your code

def calculate_smoothie_price(price_banana, price_strawberry):
    smoothie_price = (price_banana + price_strawberry) * 2
    # as per Sara Cunningham's email @ 2020-10-12, 2 is the number of portions per month
    return smoothie_price

month_1_smoothie_price = calculate_smoothie_price(price_banana=1.25, price_strawberry=3.40)
month_2_smoothie_price = calculate_smoothie_price(price_banana=1.50, price_strawberry=3.20)
month_3_smoothie_price = calculate_smoothie_price(price_banana=1.10, price_strawberry=3.60)
print(month_1_smoothie_price, month_2_smoothie_price, month_3_smoothie_price)


# And if you need to edit the way smoothie prices are calculated, you only have to change 1 line of code

def calculate_smoothie_price(price_banana, price_strawberry):
    smoothie_price = ((price_banana + price_strawberry) * 2) + 5
    # as per Sara Cunningham's email @ 2020-10-12, 2 is the number of portions per month
    # <business context explanation of why there's an add 5 at the end>
    return smoothie_price

month_1_smoothie_price = calculate_smoothie_price(price_banana=1.25, price_strawberry=3.40)
month_2_smoothie_price = calculate_smoothie_price(price_banana=1.50, price_strawberry=3.20)
month_3_smoothie_price = calculate_smoothie_price(price_banana=1.10, price_strawberry=3.60)
print(month_1_smoothie_price, month_2_smoothie_price, month_3_smoothie_price)


# As a flex that no one asked for, if you have many months' worth of prices, you could make the code more dynamic like below
def calculate_smoothie_price(price_banana, price_strawberry):
    smoothie_price = (price_banana + price_strawberry) * 2
    # as per Sara Cunningham's email @ 2020-10-12, 2 is the number of portions per month
    return smoothie_price

banana_prices = {1: 1.25,
                 2: 1.50,
                 3: 1.10}

strawberry_prices = {1: 3.40,
                     2: 3.20,
                     3: 3.60}

smoothie_prices = {} # Instantiate a new dictionary
month = 1 # Start from month 1

# For each month, calculate the price of smoothies
for price_banana, price_strawberry in zip(banana_prices.values(), strawberry_prices.values()):
    smoothie_prices[month] = calculate_smoothie_price(price_banana, price_strawberry)
    month += 1

print(smoothie_prices)

###############################################################

# Storytime: I eat a cheese toasty every Wednesday (because Wednesdays suck and cheese toasties make everything better) and have a very specific recipe for it.
# I want to know, assuming that prices for ingredients change every month (but not within the month) how much my cheese toasties will cost me each month
# Also assume that each month has 4 weeks (4 Wednesdays) for simplicity's sake

# Exercise: Using the below information, write a function that will tell me how much my cheese toastes will cost me in a month. It needs to be flexible to take into account that the prices change every month

# The recipe: 2 slices of bread, 1 slice of cheese, 1 teaspoon of mustard - you can be fancy and make assumptions like how many slices are in a loaf of bread but that's not really the point of this exercise

# In September, the prices of ingredients are as below - btw, as you might've guessed, you can give a dictionary as an input into a function
prices = {'cheese': 4.50,
          'mustard': 3.40,
          'bread': 1.25}

# In October, the prices of ingredients are as below
prices = {'cheese': 4.60,
          'mustard': 3.40,
          'bread': 1.20}

# Write your function here





# P.S. the cheese toasties are a lie. I'm lactose-intolerant


