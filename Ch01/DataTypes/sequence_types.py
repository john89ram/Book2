# Strings - a string is a sequence of characters, and it is one of the fundamental 
# data types. Strings are used to represent textual data. You can create a string 
# by enclosing a sequence of characters within single quotes (') or double quotes ("). 

string_single_quote = 'Hello, World!\n'
#                                    ^
# Here the \n means create a new line
string_double_quote = "Python is AWESOME!"
print(string_single_quote, string_double_quote)

# Here are some more formatting shortcuts
# \t : Tab
print("First\tSecond\tThird")

# \r : Carriage Return - It is used to move the cursor to the beginning of the line.
print("Hello\rWorld")
# It returns to the start of the line and writes over "Hello".

# \\ : Backslash
print("This is a backslash: \\")

# \' and \": Single and Double Quotes- Represent single and double quote characters.
print("Single quote: \'\nDouble quote: \"")

# \b : Backspace
print("Hello\bWorld")
# Same as \\, however this one will only go back one space. 

# \f : Form Feed - It is used to start a new page.
print("Page 1\fPage 2")
#-----------------------------------------------------------------------------------

# List - a list is a versatile and mutable (modifiable) data type that represents 
# an ordered collection of elements. Lists are one of the most commonly used data 
# structures in Python. You can create a list by enclosing a sequence of elements 
# within square brackets [].
my_list = [1, 2, 3, 4, 5]

# Indexing a list. Lists are indexed, and you can access individual elements by 
# their position in the list. Indexing starts at 0.
# You can use slicing to extract a sublist by specifying a range of indices.
my_list = [10, 20, 30, 40, 50]
print(my_list[0])      # Indexing - Outputs: 10
print(my_list[1:4])    # Slicing - Outputs: [20, 30, 40]

# Lists are mutable, meaning you can modify their elements, add new elements, or 
# remove existing ones.
my_list = [1, 2, 3]
print(my_list)

my_list[1] = 5         # Modifying an element in index 1
print(my_list)

my_list.append(6)      # Appending a new element at the end of the list
print(my_list)

del my_list[0]         # Deleting an element in index 0 
print(my_list)

# Extra list modifying methods commands.
# extend() - Extends the list with another list.
    # Can also concatenate list with '+'
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined_list = list2 + list1
print(combined_list)
# insert() - Inserts an element at an assigned index.
# remove() - Removes the first instance of the assigned value.
# pop() - Used to remove and return an element from a specific index in a list. 
# count() - Count the number of occurrences of a specified element in a list.
# index() - Index used to find the index of the first occurrence assigned element.

# len() - method used to count the elements within a list.

# Nesting a list can contain other lists, enabling the creation of nested data structures.
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(nested_list)