# String Manipulation & Tuple Conversion
# Given the following string:
# value = "python is high level programming language"
# Write a Python program to:

# Capitalize the first letter of each word

# Split the string into individual words

# Convert the result into a tuple of these capitalized words
# OutPut =("Python", "Is", "High", "Level", "Programming","Language")

value = "python is high level programming language"
capital = value.title()
print("\nTitle:", capital)

list1 = value.split()
print("List:", list1)

print("Tuple:", tuple(list1))

# Task:
# Get day name from user number input (1-7), 
# where 1 = Sunday, 
# 2 = Monday, ..., 
# 7 = Saturday

day = {
    "1" : "Sunday",
    "2" : "Monday",
    "3" : "Tuseday",
    "4" : "Wednesday",
    "5" : "Thursday",
    "6" : "Friday",
    "7" : "Saturday"
}
num = input("\nEnter any number: ")
print("Day:", day.get(num, "Not Found"))


# Given the dictionary person = {'name': 'sujan', 'age': 23, 'city': 'Kathmandu'}, 
# add a new key-value pair 'job': 'Developer' to the dictionary. 
# Then update the value of the 'name' key to 'Ram Bahadur' and 'age' to 29.

person = {'name': 'sujan', 'age': 23, 'city': 'Kathmandu'}
print("\nPerson:", person)

person['job'] = 'Developer'
print("Add:", person)

# person['name'] = 'Ram Bahadur'
# person['age'] = 29

person.update({'name': 'Ram Bahadur', 'age' : 29})
print("Update: ", person)


# Given a dictionary:
# my_details = {
#     'name':'sujan',
#     'grade': 0,
#     'address':'ktm',
#     'hobbies':{
#         'sports':'running',
#         'game':'pubg',
#         'novel':'xyz',
#         'anime':'one piece',
#     },
#     'email':'sujan@gmail.com'
# }
# Change the value of 'novel' key from 'xyz' to 'Harry Potter'

print("\nDictionary")
my_details = {
    'name':'sujan',
    'grade': 0,
    'address':'ktm',
    'hobbies':{
        'sports':'running',
        'game':'pubg',
        'novel':'xyz',
        'anime':'one piece',
    },
    'email':'sujan@gmail.com'
}
# my_details['hobbies']['novel'] = 'Harry Potter'
my_details['hobbies'].update({'novel': 'Harry Potter'})
print(my_details)

print("")