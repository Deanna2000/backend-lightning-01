# Lightning Exercise July 6, 2018 - Python Functions

* Write a function that takes a list, a number, and a string as args.
* The string parameter should have a default value.
* In the function body, loop over the list and output the items.
*  Use slice to loop through only the first n items in the array, where n = the value of the second argument.
* Each item should be prefaced by value of the string argument
   * One example output might then be "I have visited the city of San Francisco" if "San Francisco" was an item in the list, and the string argument was "I have visited the city of "
* Try it out! Execute the function both with and without passing in a value for the string parameter

## What the output looks like:
```
➜  ltng-01 git:(master) ✗ python drinks.py
The List with the provided (love) string
This will generate the entire list of items
I love to drink coffee
I love to drink latte
I love to drink iced tea
I love to drink matcha
I love to drink tumeric milk
This is the sliced list of items
I love to drink coffee
I love to drink latte
I love to drink iced tea

The List with the default (hate) string
This will generate the entire list of items
I hate to drink coffee
I hate to drink latte
I hate to drink iced tea
I hate to drink matcha
I hate to drink tumeric milk
This is the sliced list of items
I hate to drink coffee
I hate to drink latte
I hate to drink iced tea
➜  ltng-01 git:(master) ✗
```