'''
Python Exercises 1 - basics, for loops, lists, dictionaries
Author: github.com/mei-yong
Date Updated: 2020-10-24
'''

###############################################################

# Fix this
new_sentence = "The cashier was very confused when he brought " + 14 + tubs of vaseline to the checkout
print(new_sentence)

###############################################################

# Example variable assignments

# This...
a = 74
b = 30
print(a,b)

# Is the same as this...
a, b = 74, 30
print(a,b)

###############################################################

# Example of print(f"string") - only available in python version 3.6 onwards
food_item = "potatoes"
num_food_item = 5
print(f"There are {num_food_item} {food_item} on the sofa")

###############################################################

# Example of a list and how to call on elements in a list - remember that python list indexes start from zero i.e. [0, 1, 2, 3, etc]
answers = ['throne', 'army', 'you', 'the Earth']

print(f"There's no {answers[0]}, there is no version of this where you come out on top. Maybe your {answers[1]} comes and maybe it's too much for us but it's all on {answers[2]}. Because if we can't protect {answers[3]}, you can be damned well sure we'll avenge it!")

###############################################################

# Fix this - there are 4 errors
print(f"There's no {answers[1]}, there is no version of this where you come out on top. Maybe your {answers} comes and maybe it's too much for us but it's all on {answers[6]}. Because if we can't protect answers[3], you can be damned well sure we'll avenge it!")

###############################################################

# Example of a dictionary and how to call on elements in a dictionary
# Terminology-wise...
# answers is a variable that holds the dictionary
# 'type_of_seating_furniture' is a key
# 'throne' is a value
answers = {'type_of_seating_furniture': 'throne',
           'group_of_people': 'army',
           'a_person': 'you',
           'a_planet': 'the Earth'}

print(f"There's no {answers['type_of_seating_furniture']}, there is no version of this where you come out on top. Maybe your {answers['group_of_people']} comes and maybe it's too much for us but it's all on {answers['a_person']}. Because if we can't protect {answers['a_planet']}, you can be damned well sure we'll avenge it!")

###############################################################

# Fix this - there are 4 errors
print(f"There's no {answers[type_of_seating_furniture]}, there is no version of this where you come out on top. Maybe your {'group_of_people'} comes and maybe it's too much for us but it's all on {a_person}. Because if we can't protect answers['a_planet'], you can be damned well sure we'll avenge it!")

###############################################################

# Run this line to instantiate the some_numbers list to be used in later exercises
some_numbers = [1, 2, 3, 5, 8, 13, 21, 34]

# Loop through some_numbers and print out the numbers - below is syntax for guidance, replace pass with a print statement
for number in some_numbers:
    pass

###############################################################

# Loop through some_numbers and only print out the even numbers - you might want to use an if statement


###############################################################

# Example syntax for the .append() method
list_a = [1,2,3]
print(f"This is the list before appending any new values: {a_list}")

list_a.append(4)
print(f"This is the list after appending any new values: {a_list}")

###############################################################

# Note that you can add lists together
list_a = [1,2,3]
list_b = [4,5,6]
list_c = list_a + list_b
print(list_c)

###############################################################

# Loop through some_numbers and if the number is odd, add the string value "marco" to a new list and if it's even, add "polo" to the new list
# i.e. return ["marco", "polo", "marco", "marco", "polo", "marco", "marco", "polo"]
# You might want to use the .append() method
new_list = []
for number in some_numbers:
    pass

###############################################################

# Using a loop through some_numbers, return a new list where all the numbers are raised by 1 - i.e. return [2, 3, 4, 6, 9, 14, 22, 35]
# Similar to the previous question, you might want to use the .append() method
some_numbers_plus_one = []
for number in some_numbers:
    pass

print(some_numbers_plus_one)

###############################################################

# Example syntax - same as above but using list comprehension which runs a lot faster than a for loop
some_numbers_plus_one = [number + 1 for number in some_numbers]
print(some_numbers_plus_one)

###############################################################

# Using list comprehension, return a new list variable called some_numbers_plus_two where all the numbers are raised by 2

# write your answer here
print(some_numbers_plus_two)

###############################################################

# Run these lines to instantiate the superheroes dictionary to be used in later exercises
superheroes = {'Iron Man': 'Tony Stark',
               'Captain America': 'Steve Rogers',
               'Spiderman': 'Peter Parker'}

# Example of how to loop through keys and values in a dictionary - must use the .items() method
for key, value in superheroes.items():
    print(f"{key}'s civilian name is {value}")

###############################################################

# On a side note, try to guess what each of these prints will output and then run the print to find out

x = superheroes
print (x)
# Q: so what is x? What datatype is it?

for x in superheroes:
    print(x)
# Q: so what is x? What datatype is it?

for x in superheroes.keys():
    print(x)
# Q: so what is x? What datatype is it?

for x in superheroes.values():
    print(x)
# Q: so what is x? What datatype is it?

###############################################################

# Example syntax for how to add a new entry to a dictionary
print(f"Remember that this is the superheroes dictionary we're working with: {superheroes}")

superheroes['Deadpool'] = 'Wade Wilson'
# P.S. you can argue that Deadpool's an anti-hero or whatever all you want but I think he's awesome and so he will be included in this exercise

print(f"This is what the superheroes dictionary looks like after adding a new entry: {superheroes}")

###############################################################

# Note that unlike lists, you cannot add dictionaries together
dict_a = {'a':1}
dict_b = {'b':2}
dict_c = dict_a + dict_b
print(dict_c)

###############################################################

# Add a new entry in the dictionary for another superhero of your choice

# write your answer here
print(superheroes)

###############################################################

# Run these lines to instantiate the new_hero_names and new_civilian_names lists to be used in later exercises
new_hero_names = ['Batman', 'Wonder Woman']
new_civilian_names = ['Bruce Wayne', 'Diana Prince']

# Example of how to loop through 2 lists at the same time
for hero_name, civilian_name in zip(new_hero_names, new_civilian_names):
    print(hero_name, civilian_name)

###############################################################

# Add 2 new entries to the superheroes dictionary using new_hero_names and new_civilian_names lists

# write your answer here
print(superheroes)

###############################################################

# Run these lines to instantiate the food_items dictionary to be used in later exercises
food_items = {"some_fruits": ["watermelon", "peach", "strawberry"],
               "some_veg": ["cabbage", "broccoli", "cucumber"]}

# Add "banana" to the some_fruits list and add "onion" to the some_veg list
# i.e. return {'some_fruits': ['watermelon', 'peach', 'strawberry', 'banana'], 'some_veg': ['cabbage', 'broccoli', 'cucumber', 'onion']}
# this last exercise pulls together all the previous exercises - if statements, looping through and manipulating the data in dictionaries and lists
# if you got stuck on any previous ones, you likely won't be able to do this one - at this point, let me know and we can walk through the whole sheet together

# write your answer here
print(food_items)

###############################################################

# Example error handling syntax
some_potatoes = ["fries", "wedges", "hashbrowns"]

try:
    potato_item = some_potatoes[3]
except:
    print("This is an error message related to potatoes")