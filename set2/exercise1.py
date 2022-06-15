"""
Commenting skills:

TODO: above every line of code comment what you THINK the line below does.
TODO: execute that line and write what actually happened next to it.

See example for first print statement
"""
import platform

# I think this will print "hello! Let's get started" by calling the print function.
print("hello! Let's get started")  # it printed "hello! Let's get started"
# This initialises a list with fixed values
some_words = ['what', 'does', 'this', 'line', 'do', '?'] # It initialised a list with values
# it loops over every entry in list some_words and prints it to screen
for word in some_words: # for loop over list
    print(word) # print each entry
# it loops over every entry in list some_words and prints it to screen
for x in some_words: # for loop over list
    print(x)# print each entry
# this prints the entire list
print(some_words) # printed the entire list
# check if list is longer then 3 entries
if len(some_words) > 3: # chek if length of list is bigger then 3
    print('some_words contains more than 3 words') #if so print message
# defines a method with no args
def usefulFunction():
    """
    You may want to look up what uname does before you guess
    what the line below does:
    https://docs.python.org/3/library/platform.html#platform.uname
    """
    print(platform.uname()) # prints a named tuple containing system info
# calls a use full functino
usefulFunction() # called a usefull function
