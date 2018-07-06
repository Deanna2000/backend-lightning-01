def practice_function(list, number, str="I hate to drink "):
    print("This will generate the entire list of items")
    for item in list:
        print(str + item)
    print("This is the sliced list of items")
    for item in list[:number_example]:
        print(str + item)

list_of_stuff = ["coffee","latte","iced tea", "matcha", "tumeric milk"]
number_example = 3
string_thing = "I love to drink "

practice_function(list_of_stuff, number_example, string_thing)
practice_function(list_of_stuff, number_example)

