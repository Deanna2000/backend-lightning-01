# Set up a function to accept parameters of a list, number and string
def practice_function(list, number, str="I hate to drink "):
    # Loop through the list and print each item
    print("This will generate the entire list of items")
    for item in list:
        print(str + item)
    # Loop through the list n times based on the number parameter
    print("This is the sliced list of items")
    for item in list[:number_example]:
        print(str + item)

# Populate parameter variables
list_of_stuff = ["coffee","latte","iced tea", "matcha", "tumeric milk"]
number_example = 3
string_thing = "I love to drink "

# Call the function with and without the string variable
print("The List with the provided (love) string")
practice_function(list_of_stuff, number_example, string_thing)
print("")
print("The List with the default (hate) string")
practice_function(list_of_stuff, number_example)

