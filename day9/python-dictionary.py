programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.", 
"Function": "A piece of code that you can easily call over and over and over again.",
}
#Retrieving items from the dictionary
# print(programming_dictionary["Bug"])

#Adding new items to the dictionary
programming_dictionary["Loop"] = "The action of doing something over and over again."

#Creating an empty dictionary
# empty_dictionary = {}

#Wipe an entire dictionary
# programming_dictionary = {}
# print(programming_dictionary)

#Edit an item in a dictionary
programming_dictionary["Bug"] = "A moth in your computer."
# print(programming_dictionary)

#Loop through the dictionary
for key in programming_dictionary :
  print(key)
  print(programming_dictionary[key])