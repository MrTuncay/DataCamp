#!/usr/bin/env python
# coding: utf-8

# # Python Data Science Toolbox

# ## Python Data Science Toolbox (Part 1)

# **Course Description**
# 
# It's now time to push forward and develop your Python chops even further. There are lots and lots of fantastic functions in Python and its library ecosystem. However, as a Data Scientist, you'll constantly need to write your own functions to solve problems that are dictated by your data. The art of function writing is what you'll learn in this first Python Data Science toolbox course. You'll come out of this course being able to write your very own custom functions, complete with multiple parameters and multiple return values, along with default arguments and variable-length arguments. You'll gain insight into scoping in Python and be able to write lambda functions and handle errors in your very own function writing practice. On top of this, you'll wrap up each Chapter by diving into using your acquired skills to write functions that analyze twitter DataFrames and are generalizable to broader Data Science contexts.
# 
# 

# ## 1. Writing your own functions
# 
# Here you will learn how to write your very own functions. In this Chapter, you'll learn how to write simple functions, as well as functions that accept multiple arguments and return multiple values. You'll also have the opportunity to apply these newfound skills to questions that commonly arise in Data Science contexts.

# ### 1.1 Strings in Python
# In the video, you learned of another standard Python datatype, strings. Recall that these represent textual data. To assign the string 'DataCamp' to a variable company, you execute:

# In[1]:


import warnings
warnings.filterwarnings('ignore')

company = 'DataCamp'


# You've also learned to use the operations `+` and `*` with strings. Unlike with numeric types such as ints and floats, the `+` operator concatenates strings together, while the `*` concatenates multiple copies of a string together. In this exercise, you will use the `+` and `*` operations on strings to answer the question below. Execute the following code in the shell:

# In[2]:


object1 = "data" + "analysis" + "visualization"
object2 = 1 * 3
object3 = "1" * 3


# In[3]:


print(object1, object2, object3)


# ### 1.2 Recapping built-in functions
# In the video, Hugo briefly examined the return behavior of the built-in functions `print()` and `str()`. Here, you will use both functions and examine their return values. A variable `x` has been preloaded for this exercise. Run the code below in the console. Pay close attention to the results to answer the question that follows.
# 
# * Assign `str(x)` to a variable `y1`: `y1 = str(x)`
# * Assign `print(x)` to a variable `y2`: `y2 = print(x)`  
# * Check the types of the variables `x`, `y1`, and `y2`. 
# 
# What are the types of `x`, `y1`, and `y2`?  

# In[4]:


x = 4.89
y1 = str(x)
y2 = print(x)


# In[5]:


type(x)


# In[6]:


type(y1)


# In[7]:


type(y2)


# *It is important to remember that assigning a variable y2 to a function that prints a value but does not return a value will result in that variable y2 being of type NoneType*

# ### 1.3 Write a simple function
# In the last video, Hugo described the basics of how to define a function. You will now write your own function!
# 
# Define a function, shout(), which simply prints out a string with three exclamation marks '!!!' at the end. The code for the square() function that we wrote earlier is found below. You can use it as a pattern to define shout().

# In[8]:


def square():
    new_value = 4 ** 2
    return new_value


# **Instructions**
# 
# * Complete the function header by adding the appropriate function name, `shout`.
# * In the function body, **concatenate** the string, `'congratulations'` with another string, `'!!!'`. Assign the result to `shout_word`.
# * Print the value of `shout_word`.
# * Call the `shout` function.

# In[9]:


# Define the function shout
def shout():
    """Print a string with three exclamation marks"""
    # Concatenate the strings: shout_word
    shout_word = 'congratulations' + '!!!'

    # Print shout_word
    print(shout_word)

# Call shout
shout()


# ### 1.4 Single-parameter functions
# Congratulations! You have successfully defined and called your own function! That's pretty cool.
# 
# In the previous exercise, you defined and called the function `shout()`, which printed out a string concatenated with `'!!!'`. You will now update `shout()` by adding a parameter so that it can accept and process any string argument passed to it. Also note that `shout(word)`, the part of the header that specifies the function name and parameter(s), is known as the signature of the function. You may encounter this term in the wild!

# **Instructions**
# 
# * Complete the function header by adding the parameter name, word.
# * Assign the result of concatenating word with '!!!' to shout_word.
# * Print the value of shout_word.
# * Call the shout() function, passing to it the string, 'congratulations'.

# In[10]:


# Define shout with the parameter, word
def shout(word):
    """Print a string with three exclamation marks"""
    # Concatenate the strings: shout_word
    shout_word = word + '!!!'

    # Print shout_word
    print(shout_word)

# Call shout with the string 'congratulations'
shout('congratulations')


# ### 1.5 Functions that return single values
# You're getting very good at this! Try your hand at another modification to the `shout()` function so that it now *returns* a single value instead of printing within the function. Recall that the `return` keyword lets you return values from functions. Parts of the function `shout()`, which you wrote earlier, are shown. Returning values is generally more desirable than printing them out because, as you saw earlier, a `print()` call assigned to a variable has type `NoneType`.
# 
# **Instructions**
# 
# * In the function body, concatenate the string in `word` with `'!!!'` and assign to shout_word.
# * Replace the `print()` statement with the appropriate `return` statement.
# * Call the `shout()` function, passing to it the string, `'congratulations'`, and assigning the call to the variable, yell.
# * To check if `yell` contains the value returned by `shout()`, print the value of `yell`.

# In[11]:


# Define shout with the parameter, word
def shout(word):
    """Return a string with three exclamation marks"""
    # Concatenate the strings: shout_word
    shout_word = word + '!!!'

    # Replace print with return
    return shout_word

# Pass 'congratulations' to shout: yell
yell = shout('congratulations')

# Print yell
print(yell)


# Great work! Here it made sense to assign the output of `shout('congratulations')` to a variable `yell` because the function shout actually returns a value, it does not merely print one.

# ### 1.6 Functions with multiple parameters
# Hugo discussed the use of multiple parameters in defining functions in the last lecture. You are now going to use what you've learned to modify the `shout()` function further. Here, you will modify `shout()` to accept two arguments. Parts of the function `shout()`, which you wrote earlier, are shown.
# 
# **Instructions**
# 
# * Modify the function header such that it accepts two parameters, `word1` and `word2`, in that order.
# * Concatenate each of `word1` and `word2` with `'!!!'` and assign to `shout1` and `shout2`, respectively.
# * Concatenate `shout1` and `shout2` together, in that order, and assign to `new_shout`.
# * Pass the strings `'congratulations'` and `'you'`, in that order, to a call to `shout()`. Assign the return value to `yell`.
# 

# In[12]:


# Define shout with parameters word1 and word2
def shout(word1, word2):
    """Concatenate strings with three exclamation marks"""
    # Concatenate word1 with '!!!': shout1
    shout1 = word1 + '!!!'
    
    # Concatenate word2 with '!!!': shout2
    shout2 = word2 + '!!!'
    
    # Concatenate shout1 with shout2: new_shout
    new_shout = shout1 + shout2

    # Return new_shout
    return new_shout

# Pass 'congratulations' and 'you' to shout(): yell
yell = shout('congratulations', 'you')

# Print yell
print(yell)


# ### 1.7 A brief introduction to tuples
# Alongside learning about functions, you've also learned about tuples! Here, you will practice what you've learned about tuples: how to construct, unpack, and access tuple elements. Recall how Hugo unpacked the tuple `even_nums` in the video:
# 
# `a, b, c = even_nums`
# 
# A three-element tuple named `nums` has been preloaded for this exercise. Before completing the script, perform the following:
# 
# * Print out the value of `nums` in the IPython shell. Note the elements in the tuple.
# * In the IPython shell, try to change the first element of `nums` to the value 2 by doing an assignment: `nums[0] = 2`. What happens?
# 
# **Instructions**
# 
# * Unpack nums to the variables `num1`, `num2`, and `num3`.
# * Construct a new tuple, `even_nums` composed of the same elements in `nums`, but with the 1st element replaced with the value, 2.

# In[13]:


nums = (2, 4, 6)
# Unpack nums into num1, num2, and num3
num1, num2, num3 = nums

# Construct even_nums
even_nums = (2, num2 , num3)


# In[14]:


print(even_nums)


# ### 1.8 Functions that return multiple values
# In the previous exercise, you constructed tuples, assigned tuples to variables, and unpacked tuples. Here you will return multiple values from a function using tuples. Let's now update our `shout()` function to return multiple values. Instead of returning just one string, we will return two strings with the string `!!!` concatenated to each.
# 
# Note that the return statement `return x, y` has the same result as `return (x, y)`: the former actually packs `x` and `y` into a tuple under the hood!
# 
# **Instructions**
# 
# * Modify the function header such that the function name is now `shout_all`, and it accepts two parameters, `word1` and `word2`, in that order.
# * Concatenate the string `'!!!'` to each of `word1` and `word2` and assign to `shout1` and `shout2`, respectively.
# * Construct a tuple shout_words, composed of `shout1` and `shout2`.
# * Call `shout_all()` with the strings `'congratulations'` and `'you'` and assign the result to `yell1` and `yell2` (remember, `shout_all()` returns 2 variables!).

# In[15]:


# Define shout_all with parameters word1 and word2
def shout_all(word1, word2):
    
    # Concatenate word1 with '!!!': shout1
    shout1 = word1 + '!!!'
    
    # Concatenate word2 with '!!!': shout2
    shout2 = word2 + '!!!'
    
    # Construct a tuple with shout1 and shout2: shout_words
    shout_words = (shout1, shout2)

    # Return shout_words
    return shout_words

# Pass 'congratulations' and 'you' to shout_all(): yell1, yell2
yell1, yell2 = shout_all('congratulations','you')

# Print yell1 and yell2
print(yell1)
print(yell2)


# ### 1.9 Bringing it all together (1)
# You've got your first taste of writing your own functions in the previous exercises. You've learned how to add parameters to your own function definitions, return a value or multiple values with tuples, and how to call the functions you've defined.
# 
# In this and the following exercise, you will bring together all these concepts and apply them to a simple data science problem. You will load a dataset and develop functionalities to extract simple insights from the data.
# 
# For this exercise, your goal is to recall how to load a dataset into a DataFrame. The dataset contains Twitter data and you will iterate over entries in a column to build a dictionary in which the keys are the names of languages and the values are the number of tweets in the given language. The file `tweets.csv` is available in your current directory.
# 
# **Instuctions**
# 
# * Import the pandas package with the alias `pd`.
# * Import the file `'tweets.csv'` using the pandas function `read_csv()`. Assign the resulting DataFrame to `df`.
# * Complete the for loop by iterating over `col`, the `'lang'` column in the DataFrame `df`.
# * Complete the bodies of the `if-else` statements in the `for` loop: **if** the key is in the dictionary `langs_count`, add `1` to its current value, **else** add the key to `langs_coun` and set its value to `1`. Use the loop variable `entry` in your code.

# In[16]:


from platform import python_version
print(python_version())

import pandas as pd


# In[17]:


# Import pandas
import pandas as pd

# Import Twitter data as DataFrame: df
df = pd.read_csv('Data/tweets.csv')

# Initialize an empty dictionary: langs_count
langs_count = {}

# Extract column from DataFrame: col
col = df['lang']

# Iterate over lang column in DataFrame
for entry in col:

    # If the language is in langs_count, add 1
    if entry in langs_count.keys():
        langs_count[entry] += 1
    # Else add the language to langs_count, set the value to 1
    else:
        langs_count[entry] = 1

# Print the populated dictionary
print(langs_count)


# ### 1.10 Bringing it all together (2)
# Great job! You've now defined the functionality for iterating over entries in a column and building a dictionary with keys the names of languages and values the number of tweets in the given language.
# 
# In this exercise, you will define a function with the functionality you developed in the previous exercise, return the resulting dictionary from within the function, and call the function with the appropriate arguments.
# 
# For your convenience, the pandas package has been imported as `pd` and the `'tweets.csv'` file has been imported into the `tweets_df` variable.
# 
# **Instructions**
# 
# * Define the function `count_entries()`, which has two parameters. The first parameter is `df` for the DataFrame and the second is `col_name` for the column name.
# * Complete the bodies of the `if-else` statements in the `for` loop: **if** the key is in the dictionary `langs_count`, add `1` to its current value, **else** add the key to `langs_count` and set its value to `1`. Use the loop variable entry in your code.
# * Return the `langs_count` dictionary from inside the `count_entries()` function.
# * Call the `count_entries()` function by passing to it `tweets_df` and the name of the column, `'lang'`. Assign the result of the call to the variable `result`.

# In[18]:


tweets_df = pd.read_csv('Data/tweets.csv')

# Define count_entries()
def count_entries(df, col_name):
    """Return a dictionary with counts of 
    occurrences as value for each key."""

    # Initialize an empty dictionary: langs_count
    langs_count = {}
    
    # Extract column from DataFrame: col
    col = df[col_name]
    
    # Iterate over lang column in DataFrame
    for entry in col:

        # If the language is in langs_count, add 1
        if entry in langs_count.keys():
            langs_count[entry] += 1 
        # Else add the language to langs_count, set the value to 1
        else:
            langs_count[entry] = 1

    # Return the langs_count dictionary
    return langs_count

# Call count_entries(): result
result = count_entries(tweets_df, 'lang')

# Print the result
print(result)


# ## 2. Default arguments, variable-length arguments and scope
# 
# In this chapter, you'll learn to write functions with default arguments, so that the user doesn't always need to specify them, and variable-length arguments, so that they can pass to your functions an arbitrary number of arguments. These are both incredibly useful tools! You'll also learn about the essential concept of scope. Enjoy!
# 

# ### 2.1 Pop quiz on understanding scope
# In this exercise, you will practice what you've learned about scope in functions. The variable `num` has been predefined as `5`, alongside the following function definitions:
# ```python
# num = 5
# def func1():
#     num = 3
#     print(num)
# 
# def func2():
#     global num
#     double_num = num * 2
#     num = 6
#     print(double_num)
# ``` 
# 
# Try calling `func1()` and `func2()` in the shell, then answer the following questions:
# 
# * What are the values printed out when you call `func1()` and `func2()`?
# * What is the value of `num` in the global scope after calling `func1()` and `func2()`?

# In[19]:


num = 5
def func1():
    num = 3
    print(num)

def func2():
    global num
    double_num = num * 2
    num = 6
    print(double_num)
    
func1()
func2()
print(num)


# `func1()` prints out `3`, f`unc2()` prints out `10`, and the value of `num` in the global scope is `6`.

# ### 2.1 The keyword global
# Let's work more on your mastery of scope. In this exercise, you will use the keyword `global` within a function to alter the value of a variable defined in the global scope.
# 
# __Instructions__
# 
# * Use the keyword `global` to alter the object `team` in the global scope.
# * Change the value of `team` in the global scope to the string `"justice league"`. Assign the result to `team`.
# * Hit the Submit button to see how executing your newly defined function `change_team()` changes the value of the name `team`!
# 

# In[20]:


# Create a string: team
team = "teen titans"

# Define change_team()
def change_team():
    """Change the value of the global variable team."""

    # Use team in global scope
    global team

    # Change the value of team in global: team
    team = "justice league"
# Print team
print(team)

# Call change_team()
change_team()

# Print team
print(team)


# ### 2.2 Python's built-in scope
# Here you're going to check out Python's built-in scope, which is really just a built-in module called `builtin`s. However, to query `builtins`, you'll need to `import builtins` 'because the name builtins is not itself built in...No, I’m serious!' (Learning Python, 5th edition, Mark Lutz). After executing import builtins in the IPython Shell, execute dir(builtins) to print a list of all the names in the module builtins. Have a look and you'll see a bunch of names that you'll recognize! Which of the following names is NOT in the module builtins?

# 'array'

# ### 2.3 Nested Functions I
# You've learned in the last video about nesting functions within functions. One reason why you'd like to do this is to avoid writing out the same computations within functions repeatedly. There's nothing new about defining nested functions: you simply define it as you would a regular function with `def` and embed it inside another function!
# 
# In this exercise, inside a function `three_shouts()`, you will define a nested function `inner()` that concatenates a string object with `!!!`. `three_shouts()` then returns a tuple of three elements, each a string concatenated with `!!!` using `inner()`. Go for it!
# 
# __Instructions__
# 
# * Complete the function header of the nested function with the function name `inner()` and a single parameter word.
# * Complete the return value: each element of the tuple should be a call to `inner()`, passing in the parameters from `three_shouts()` as arguments to each call.

# In[21]:


# Define three_shouts
def three_shouts(word1, word2, word3):
    """Returns a tuple of strings
    concatenated with '!!!'."""

    # Define inner
    def inner(word):
        """Returns a string concatenated with '!!!'."""
        return word + '!!!'

    # Return a tuple of strings
    return (inner(word1), inner(word2), inner(word3))

# Call three_shouts() and print
print(three_shouts('a', 'b', 'c'))


# ### 2.4 Nested Functions II
# Great job, you've just nested a function within another function. One other pretty cool reason for nesting functions is the idea of a closure. This means that the nested or inner function remembers the state of its enclosing scope when called. Thus, anything defined locally in the enclosing scope is available to the inner function even when the outer function has finished execution.
# 
# Let's move forward then! In this exercise, you will complete the definition of the inner function `inner_echo()` and then call `echo()` a couple of times, each with a different argument. Complete the exercise and see what the output will be!
# 
# __Instructions__
# 
# * Complete the function header of the inner function with the function name `inner_echo()` and a single parameter `word1`.
# * Complete the function `echo()` so that it returns `inner_echo`.
# * We have called `echo()`, passing 2 as an argument, and assigned the resulting function to `twice`. Your job is to call `echo()`, passing 3 as an argument. Assign the resulting function to `thrice`.
# * Hit Submit to call `twice()` and `thrice()` and print the results.

# In[22]:


# Define echo
def echo(n):
    """Return the inner_echo function."""

    # Define inner_echo
    def inner_echo(word1):
        """Concatenate n copies of word1."""
        echo_word = word1 * n
        return echo_word

    # Return inner_echo
    return inner_echo

# Call echo: twice
twice = echo(2)

# Call echo: thrice
thrice = echo(3)

# Call twice() and thrice() then print
print(twice('hello'), thrice('hello'))


# ### 2.5 The keyword nonlocal and nested functions
# Let's once again work further on your mastery of scope! In this exercise, you will use the keyword `nonlocal` within a nested function to alter the value of a variable defined in the enclosing scope.
# 
# __Instructions__
# 
# * Assign to `echo_word` the string `word`, concatenated with itself.
# * Use the keyword `nonlocal` to alter the value of `echo_word` in the enclosing scope.
# * Alter `echo_word` to `echo_word` concatenated with '!!!'.
# * Call the function `echo_shout()`, passing it a single argument 'hello'.

# In[23]:


# Define echo_shout()
def echo_shout(word):
    """Change the value of a nonlocal variable"""
    
    # Concatenate word with itself: echo_word
    echo_word = word * 2
    
    # Print echo_word
    print(echo_word)
    
    # Define inner function shout()
    def shout():
        """Alter a variable in the enclosing scope"""    
        # Use echo_word in nonlocal scope
        nonlocal echo_word
        
        # Change echo_word to echo_word concatenated with '!!!'
        echo_word = echo_word + '!!!'
    
    # Call function shout()
    shout()
    
    # Print echo_word
    print(echo_word)

# Call function echo_shout() with argument 'hello'
echo_shout('hello')


# ### 2.6 Functions with one default argument
# In the previous chapter, you've learned to define functions with more than one parameter and then calling those functions by passing the required number of arguments. In the last video, Hugo built on this idea by showing you how to define functions with default arguments. You will practice that skill in this exercise by writing a function that uses a default argument and then calling the function a couple of times.
# 
# __Instructions__
# 
# * Complete the function header with the function name `shout_echo`. It accepts an argument `word1` and a default argument `echo` with default value `1`, in that order.
# * Use the `*` operator to concatenate `echo` copies of `word1`. Assign the result to `echo_word`.
# * Call `shout_echo()` with just the string, `"Hey"`. Assign the result to `no_echo`.
# * Call `shout_echo()` with the string `"Hey"` and the value `5` for the default argument, `echo`. Assign the result to `with_echo`.

# In[24]:


# Define shout_echo
def shout_echo(word1, echo=1):
    """Concatenate echo copies of word1 and three
     exclamation marks at the end of the string."""

    # Concatenate echo copies of word1 using *: echo_word
    echo_word = word1 * echo

    # Concatenate '!!!' to echo_word: shout_word
    shout_word = echo_word + '!!!'

    # Return shout_word
    return shout_word

# Call shout_echo() with "Hey": no_echo
no_echo = shout_echo("Hey")

# Call shout_echo() with "Hey" and echo=5: with_echo
with_echo = shout_echo("Hey", 5)

# Print no_echo and with_echo
print(no_echo)
print(with_echo)


# ### 2.7 Functions with multiple default arguments
# You've now defined a function that uses a default argument - don't stop there just yet! You will now try your hand at defining a function with more than one default argument and then calling this function in various ways.
# 
# After defining the function, you will call it by supplying values to all the default arguments of the function. Additionally, you will call the function by not passing a value to one of the default arguments - see how that changes the output of your function!
# 
# __Instructions__
# 
# * Complete the function header with the function name `shout_echo`. It accepts an argument `word1`, a default argument `echo` with default value `1` and a default argument `intense` with default value `False`, in that order.
# * In the body of the `if` statement, make the string object `echo_word` upper case by applying the method .upper() on it.
# * Call `shout_echo()` with the string, `"Hey"`, the value `5` for `echo` and the value `True` for `intense`. Assign the result to `with_big_echo`.
# * Call `shout_echo()` with the string `"Hey"` and the value `True` for intense. Assign the result to `big_no_echo`.

# In[25]:


# Define shout_echo
def shout_echo(word1, echo=1, intense=False):
    """Concatenate echo copies of word1 and three
    exclamation marks at the end of the string."""

    # Concatenate echo copies of word1 using *: echo_word
    echo_word = word1 * echo

    # Capitalize echo_word if intense is True
    if intense is True:
        # Capitalize and concatenate '!!!': echo_word_new
        echo_word_new = echo_word.upper() + '!!!'
    else:
        # Concatenate '!!!' to echo_word: echo_word_new
        echo_word_new = echo_word + '!!!'

    # Return echo_word_new
    return echo_word_new

# Call shout_echo() with "Hey", echo=5 and intense=True: with_big_echo
with_big_echo = shout_echo("Hey", echo=5, intense=True)

# Call shout_echo() with "Hey" and intense=True: big_no_echo
big_no_echo = shout_echo("Hey", intense=True)

# Print values
print(with_big_echo)
print(big_no_echo)


# ### 2.8 Functions with variable-length arguments (*args)
# 
# Flexible arguments enable you to pass a variable number of arguments to a function. In this exercise, you will practice defining a function that accepts a variable number of string arguments.
# 
# The function you will define is `gibberish()` which can accept a variable number of string values. Its return value is a single string composed of all the string arguments concatenated together in the order they were passed to the function call. You will call the function with a single string argument and see how the output changes with another call using more than one string argument. Recall from the previous video that, within the function definition, `args` is a tuple.
# 
# __Instructions__
# 
# * Complete the function header with the function name `gibberish`. It accepts a single flexible argument `*args`.
# * Initialize a variable `hodgepodge` to an empty string.
# * Return the variable `hodgepodge` at the end of the function body.
# * Call `gibberish()` with the single string, `"luke"`. Assign the result to `one_word`.
# * Hit the Submit button to call `gibberish()` with multiple arguments and to print the value to the Shell.

# In[26]:


# Define gibberish
def gibberish(*args):
    """Concatenate strings in *args together."""

    # Initialize an empty string: hodgepodge
    hodgepodge = ''

    # Concatenate the strings in args
    for word in args:
        hodgepodge += word

    # Return hodgepodge
    return hodgepodge

# Call gibberish() with one string: one_word
one_word = gibberish("luke")

# Call gibberish() with five strings: many_words
many_words = gibberish("luke", "leia", "han", "obi", "darth")

# Print one_word and many_words
print(one_word)
print(many_words)


# In[27]:


test = gibberish('gibberishun', 'gibberishancy', 'gibberishriends', 'gibberishork')
print(test)


# ## 2.9 Functions with variable-length keyword arguments (**kwargs)
# 
# Let's push further on what you've learned about flexible arguments - you've used `*args`, you're now going to use `**kwargs`! What makes `**kwargs` different is that it allows you to pass a variable number of keyword arguments to functions. Recall from the previous video that, within the function definition, `kwargs` is a dictionary.
# 
# To understand this idea better, you're going to use `**kwargs` in this exercise to define a function that accepts a variable number of keyword arguments. The function simulates a simple status report system that prints out the status of a character in a movie.
# 
# __Instructions_
# 
# * Complete the function header with the function name `report_status`. It accepts a single flexible argument `**kwargs`.
# * Iterate over the key-value pairs of `kwargs` to print out the keys and values, separated by a colon ':'.
# * In the first call to `report_status()`, pass the following keyword-value pairs: `name="luke"`, `affiliation="jedi"` and `status="missing"`.
# * In the second call to `report_status()`, pass the following keyword-value pairs: `name="anakin"`, `affiliation="sith lord"` and `status="deceased"`.

# In[28]:


# Define report_status
def report_status(**kwargs):
    """Print out the status of a movie character."""

    print("\nBEGIN: REPORT\n")

    # Iterate over the key-value pairs of kwargs
    for key, value in kwargs.items():
        # Print out the keys and values, separated by a colon ':'
        print(key + ": " + value)

    print("\nEND REPORT")

# First call to report_status()
report_status(name="luke", affiliation="jedi", status="missing")

# Second call to report_status()
report_status(name="anakin", affiliation="sith lord", status="deceased")


# ### 2.10 Bringing it all together (1)
# 
# Recall the Bringing it all together exercise in the previous chapter where you did a simple Twitter analysis by developing a function that counts how many tweets are in certain languages. The output of your function was a dictionary that had the language as the keys and the counts of tweets in that language as the value.
# 
# In this exercise, we will generalize the Twitter language analysis that you did in the previous chapter. You will do that by including a default argument that takes a column name.
# 
# For your convenience, `pandas` has been imported as `pd` and the `'tweets.csv'` file has been imported into the DataFrame `tweets_df`. Parts of the code from your previous work are also provided.
# 
# **Instructions**
# 
# * Complete the function header by supplying the parameter for a DataFrame `df` and the parameter `col_name` with a default value of `'lang'` for the DataFrame column name.
# * Call `count_entries()` by passing the `tweets_df` DataFrame and the column name `'lang'`. Assign the result to `result1`. Note that since `'lang'` is the default value of the `col_name` parameter, you don't have to specify it here.
# * Call `count_entries()` by passing the `tweets_df` DataFrame and the column name `'source'`. Assign the result to `result2`.
# 
# 

# In[29]:


import pandas as pd
tweets_df = pd.read_csv('Data/tweets.csv')

# Define count_entries()
def count_entries(df, col_name='lang'):
    """Return a dictionary with counts of
    occurrences as value for each key."""

    # Initialize an empty dictionary: cols_count
    cols_count = {}

    # Extract column from DataFrame: col
    col = df[col_name]
    
    # Iterate over the column in DataFrame
    for entry in col:

        # If entry is in cols_count, add 1
        if entry in cols_count.keys():
            cols_count[entry] += 1
            

        # Else add the entry to cols_count, set the value to 1
        else:
            cols_count[entry] = 1

    # Return the cols_count dictionary
    return cols_count

# Call count_entries(): result1
result1 = count_entries(tweets_df)

# Call count_entries(): result2
result2 = count_entries(tweets_df, col_name='source')

# Print result1 and result2
print(result1)
print(result2)


# ### 2.11 Bringing it all together (2)
# 
# Wow, you've just generalized your Twitter language analysis that you did in the previous chapter to include a default argument for the column name. You're now going to generalize this function one step further by allowing the user to pass it a flexible argument, that is, in this case, as many column names as the user would like!
# 
# Once again, for your convenience, `pandas` has been imported as pd and the `'tweets.csv'` file has been imported into the DataFrame `tweets_df`. Parts of the code from your previous work are also provided.
# 
# **Instructions**
# 
# * Complete the function header by supplying the parameter for the dataframe `df` and the flexible argument `*args`.
# * Complete the `for` loop within the function definition so that the loop occurs over the tuple `args`.
# * Call `count_entries()` by passing the `tweets_df` DataFrame and the column name `'lang'`. Assign the result to `result1`.
# * Call `count_entries()` by passing the `tweets_df` DataFrame and the column names `'lang'` and `'source'`. Assign the result to `result2`.

# In[30]:


# Define count_entries()
def count_entries(df, *args):
    """Return a dictionary with counts of
    occurrences as value for each key."""
    
    #Initialize an empty dictionary: cols_count
    cols_count = {}
    
    # Iterate over column names in args
    for col_name in args:
    
        # Extract column from DataFrame: col
        col = df[col_name]
    
        # Iterate over the column in DataFrame
        for entry in col:
    
            # If entry is in cols_count, add 1
            if entry in cols_count.keys():
                cols_count[entry] += 1
    
            # Else add the entry to cols_count, set the value to 1
            else:
                cols_count[entry] = 1

    # Return the cols_count dictionary
    return cols_count

# Call count_entries(): result1
result1 = count_entries(tweets_df, 'lang')

# Call count_entries(): result2
result2 = count_entries(tweets_df, 'lang', 'source')

# Print result1 and result2
print(result1)
print(result2)


# ## 3. Lambda functions and error-handling
# 
# Herein, you'll learn about lambda functions, which allow you to write functions quickly and on-the-fly. You'll also get practice at handling errors that your functions, at some point, will inevitably throw. You'll wrap up once again applying these skills to Data Science questions.

# ### 3.1 Pop quiz on lambda functions
# In this exercise, you will practice writing a simple lambda function and calling this function. Recall what you know about lambda functions and answer the following questions:
# 
# How would you write a lambda function `add_bangs` that adds three exclamation points `'!!!'` to the end of a string `a`?
# How would you call add_bangs with the argument `'hello'`?
# 
# You may use the IPython shell to test your code.
# 
# **Possible Answers**
# 
# * The lambda function definition is: `add_bangs = (a + '!!!')`, and the function call is: `add_bangs('hello')`.
# * __The lambda function definition is: `add_bangs = (lambda a: a + '!!!')`, and the function call is: `add_bangs('hello')`.__
# * The lambda function definition is: `(lambda a: a + '!!!') = add_bangs`, and the function call is: `add_bangs('hello')`.

# In[31]:


add_bangs = (lambda a: a + '!!!')
add_bangs('hello')


# ### 3.2 Writing a lambda function you already know
# 
# Some function definitions are simple enough that they can be converted to a lambda function. By doing this, you write less lines of code, which is pretty awesome and will come in handy, especially when you're writing and maintaining big programs. In this exercise, you will use what you know about lambda functions to convert a function that does a simple task into a lambda function. Take a look at this function definition:
# ~~~
# def echo_word(word1, echo):
#     """Concatenate echo copies of word1."""
#     words = word1 * echo
#     return words
# ~~~
# 
# The function `echo_word` takes 2 parameters: a string value, `word1` and an integer value, `echo`. It returns a string that is a concatenation of `echo` copies of `word1`. Your task is to convert this simple function into a lambda function.
# 
# **Instructions**
# 
# * Define the lambda function `echo_word` using the variables `word1` and `echo`. Replicate what the original function definition for `echo_word()` does above.
# * Call `echo_word()` with the string argument `'hey'` and the value `5`, in that order. Assign the call to `result`.

# In[32]:


# Define echo_word as a lambda function: echo_word
echo_word = (lambda word1, echo: word1 * echo)

# Call echo_word: result
result = echo_word('hey', 5)

# Print result
print(result)


# ### 3.3 Map() and lambda functions
# 
# So far, you've used lambda functions to write short, simple functions as well as to redefine functions with simple functionality. The best use case for lambda functions, however, are for when you want these simple functionalities to be anonymously embedded within larger expressions. What that means is that the functionality is not stored in the environment, unlike a function defined with `def`. To understand this idea better, you will use a lambda function in the context of the `map()` function.
# 
# Recall from the video that `map()` applies a function over an object, such as a list. Here, you can use lambda functions to define the function that `map()` will use to process the object. For example:
# ~~~
# nums = [2, 4, 6, 8, 10]
# 
# result = map(lambda a: a ** 2, nums)
# ~~~
# You can see here that a lambda function, which raises a value `a` to the power of 2, is passed to `map()` alongside a list of numbers, `nums`. The map object that results from the call to `map()` is stored in `result`. You will now practice the use of lambda functions with `map()`. For this exercise, you will map the functionality of the `add_bangs()` function you defined in previous exercises over a list of strings.
# 
# **Instructions**
# 
# In the `map()` call, pass a lambda function that concatenates the string `'!!!'` to a string item; also pass the list of strings, `spells`. Assign the resulting map object to `shout_spells`.
# Convert `shout_spells` to a list and print out the list.
# 

# In[33]:


# Create a list of strings: spells
spells = ["protego", "accio", "expecto patronum", "legilimens"]

# Use map() to apply a lambda function over spells: shout_spells
shout_spells = map(lambda item: item + '!!!', spells)

# Convert shout_spells to a list: shout_spells_list
shout_spells_list = list(shout_spells)

# Convert shout_spells into a list and print it
print(shout_spells_list)


# ### 3.4 Filter() and lambda functions
# 
# In the previous exercise, you used lambda functions to anonymously embed an operation within `map()`. You will practice this again in this exercise by using a lambda function with `filter()`, which may be new to you! The function `filter()` offers a way to filter out elements from a list that don't satisfy certain criteria.
# 
# Your goal in this exercise is to use `filter()` to create, from an input list of strings, a new list that contains only strings that have more than 6 characters.
# 
# **Instructions**
# 
# * In the `filter()` call, pass a lambda function and the list of strings, `fellowship`. The lambda function should check if the `number` of characters in a string member is greater than 6; use the len() function to do this. Assign the resulting filter object to `result`.
# * Convert `result` to a list and print out the list.
# 

# In[34]:


# Create a list of strings: fellowship
fellowship = ['frodo', 'samwise', 'merry', 'pippin', 'aragorn', 'boromir', 'legolas', 'gimli', 'gandalf']

# Use filter() to apply a lambda function over fellowship: result
result = filter(lambda member: len(member)>6, fellowship)

# Convert result to a list: result_list
result_list = list(result)

# Convert result into a list and print it
print(result_list)


# ### 3.5 Reduce() and lambda functions
# 
# You're getting very good at using lambda functions! Here's one more function to add to your repertoire of skills. The `reduce()` function is useful for performing some computation on a list and, unlike `map()` and `filter()`, returns a single value as a result. To use `reduce()`, you must import it from the `functools` module.
# 
# Remember `gibberish()` from a few exercises back?
# ~~~
# # Define gibberish
# def gibberish(*args):
#     """Concatenate strings in *args together."""
#     hodgepodge = ''
#     for word in args:
#         hodgepodge += word
#     return hodgepodge
# ~~~    
#     
# `gibberish()` simply takes a list of strings as an argument and returns, as a single-value result, the concatenation of all of these strings. In this exercise, you will replicate this functionality by using `reduce()` and a lambda function that concatenates strings together.
# 
# **Instructions**
# 
# * Import the `reduce` function from the `functools` module.
# * In the `reduce()` call, pass a lambda function that takes two string arguments `item1` and `item2` and concatenates them; also pass the list of strings, `stark`. Assign the result to `result`. The first argument to `reduce()` should be the lambda function and the second argument is the list `stark`.
# 

# In[35]:


# Import reduce from functools
from functools import reduce

# Create a list of strings: stark
stark = ['robb', 'sansa', 'arya', 'brandon', 'rickon']

# Use reduce() to apply a lambda function over stark: result
result = reduce((lambda item1, item2 : item1 + item2), stark)

# Print the result
print(result)


# ### 3.6 Pop quiz about errors
# 
# In the video, Hugo talked about how errors happen when functions are supplied arguments that they are unable to work with. In this exercise, you will identify which function call raises an error and what type of error is raised.
# 
# Take a look at the following function calls to len():
# ~~~
#     len('There is a beast in every man and it stirs when you put a sword in his hand.')
#     len(['robb', 'sansa', 'arya', 'eddard', 'jon'])
#     len(525600)
#     len(('jaime', 'cersei', 'tywin', 'tyrion', 'joffrey'))
# ~~~    
# 
# Which of the function calls raises an error and what type of error is raised?
# 
# **The call len(525600) raises a TypeError.**

# In[37]:


len(525600) 


# ### 3.7 Error handling with try-except
# 
# A good practice in writing your own functions is also anticipating the ways in which other people (or yourself, if you accidentally misuse your own function) might use the function you defined.
# 
# As in the previous exercise, you saw that the `len()` function is able to handle input arguments such as strings, lists, and tuples, but not int type ones and raises an appropriate error and error message when it encounters invalid input arguments. One way of doing this is through exception handling with the `try-except` block.
# 
# In this exercise, you will define a function as well as use a `try-except` block for handling cases when incorrect input arguments are passed to the function.
# 
# Recall the `shout_echo()` function you defined in previous exercises; parts of the function definition are provided in the sample code. Your goal is to complete the exception handling code in the function definition and provide an appropriate error message when raising an error.
# 
# **Instructions**
# 
# * Initialize the variables `echo_word` and `shout_words` to empty strings.
# * Add the keywords `try` and `except` in the appropriate locations for the exception handling block.
# * Use the `*` operator to concatenate `echo` copies of `word1`. Assign the result to `echo_word`.
# * Concatenate the string `'!!!'` to `echo_word`. Assign the result to `shout_words`.

# In[ ]:


# Define shout_echo
def shout_echo(word1, echo=1):
    """Concatenate echo copies of word1 and three
    exclamation marks at the end of the string."""

    # Initialize empty strings: echo_word, shout_words
    echo_word = ''
    shout_words = ''

    # Add exception handling with try-except
    try:
        # Concatenate echo copies of word1 using *: echo_word
        echo_word = word1 * echo 

        # Concatenate '!!!' to echo_word: shout_words
        shout_words = echo_word + '!!!'
    except:
        # Print error message
        print("word1 must be a string and echo must be an integer.")

    # Return shout_words
    return shout_words

# Call shout_echo
shout_echo("particle", echo="accelerator")


# ### 3.8 Error handling by raising an error
# Another way to `raise` an error is by using `raise`. In this exercise, you will add a raise statement to the `shout_echo()` function you defined before to raise an error message when the value supplied by the user to the `echo` argument is less than 0.
# 
# The call to `shout_echo()` uses valid argument values. To test and see how the `raise` statement works, simply change the value for the `echo` argument to a negative value. Don't forget to change it back to valid values to move on to the next exercise!
# 
# **Instructions**
# 
# * Complete the `if` statement by checking if the value of `echo` is *less* than 0.
# * In the body of the `if` statement, add a `raise` statement that raises a `ValueError` with message `'echo must be greater than 0'` when the value supplied by the user to echo is `less` than 0.
# 

# In[ ]:





# ### 3.9 Bringing it all together (1)
# This is awesome! You have now learned how to write anonymous functions using `lambda`, how to pass lambda functions as arguments to other functions such as `map()`, `filter()`, and `reduce()`, as well as how to write errors and output custom error messages within your functions. You will now put together these learnings to good use by working with a Twitter dataset. Before practicing your new error handling skills,in this exercise, you will write a lambda function and use `filter()` to select retweets, that is, tweets that begin with the string `'RT'`.
# 
# To help you accomplish this, the Twitter data has been imported into the DataFrame, `tweets_df`. Go for it!
# 
# **Instructions**
# 
# In the `filter()` call, pass a lambda function and the sequence of tweets as strings, `tweets_df['text']`. The lambda function should check if the first 2 characters in a tweet x are 'RT'. Assign the resulting filter object to `result`. To get the first 2 characters in a tweet `x`, use `x[0:2]`. To check equality, use a Boolean filter with `==`.
# Convert `result` to a list and print out the list.

# In[38]:


# Define shout_echo
def shout_echo(word1, echo=1):
    """Concatenate echo copies of word1 and three
    exclamation marks at the end of the string."""

    # Raise an error with raise
    if echo < 0 :
        raise  ValueError('echo must be greater than 0')

    # Concatenate echo copies of word1 using *: echo_word
    echo_word = word1 * echo

    # Concatenate '!!!' to echo_word: shout_word
    shout_word = echo_word + '!!!'

    # Return shout_word
    return shout_word

# Call shout_echo
shout_echo("particle", echo=5)


# In[39]:


# Select retweets from the Twitter DataFrame: result
result = filter(lambda x: x[0:2] == 'RT', tweets_df['text'])

# Create list from filter object result: res_list
res_list = list(result)

# Print all retweets in res_list
for tweet in res_list:
    print(tweet)


# ### 3.10 Bringing it all together (2)
# Sometimes, we make mistakes when calling functions - even ones you made yourself. But don't fret! In this exercise, you will improve on your previous work with the `count_entries()` function in the last chapter by adding a `try-except` block to it. This will allow your function to provide a helpful message when the user calls your `count_entries()` function but provides a column name that isn't in the DataFrame.
# 
# Once again, for your convenience, `pandas` has been imported as `pd` and the `'tweets.csv'` file has been imported into the DataFrame `tweets_df`. Parts of the code from your previous work are also provided.
# 
# **Instructions**
# 
# * Add a `try` block so that when the function is called with the correct arguments, it processes the DataFrame and returns a dictionary of results.
# * Add an `except` block so that when the function is called incorrectly, it displays the following error message: `'The DataFrame does not have a ' + col_name + ' column.'`

# In[40]:


# Define count_entries()
def count_entries(df, col_name='lang'):
    """Return a dictionary with counts of
    occurrences as value for each key."""

    # Initialize an empty dictionary: cols_count
    cols_count = {}

    # Add try block
    try:
        # Extract column from DataFrame: col
        col = df[col_name]
        
        # Iterate over the column in dataframe
        for entry in col:
    
            # If entry is in cols_count, add 1
            if entry in cols_count.keys():
                cols_count[entry] += 1
            # Else add the entry to cols_count, set the value to 1
            else:
                cols_count[entry] = 1
    
        # Return the cols_count dictionary
        return cols_count

    # Add except block
    except:
        'The DataFrame does not have a ' + col_name + ' column.'

# Call count_entries(): result1
result1 = count_entries(tweets_df, 'lang')

# Print result1
print(result1)


# ### 3.11 Bringing it all together (3)
# In the previous exercise, you built on your function `count_entries()` to add a `try-except` block. This was so that users would get helpful messages when calling your `count_entries()` function and providing a column name that isn't in the DataFrame. In this exercise, you'll instead raise a `ValueError` in the case that the user provides a column name that isn't in the DataFrame.
# 
# Once again, for your convenience, `pandas` has been imported as `pd` and the `'tweets.csv'` file has been imported into the DataFrame `tweets_df`. Parts of the code from your previous work are also provided.
# 
# **Instructions**
# 
# * If `col_name` is not a column in the DataFrame `df`, raise a `ValueError 'The DataFrame does not have a ' + col_name + ' column.'`.
# * Call your new function `count_entries()` to analyze the `'lang'` column of `tweets_df`. Store the result in `result1`.
# * Print `result1`. This has been done for you, so hit 'Submit Answer' to check out the result. In the next exercise, you'll see that it raises the necessary `ValueErrors`.
# 

# ### 3.12 Bringing it all together: testing your error handling skills
# You have just written error handling into your `count_entries()` function so that, when the user passes the function a column (as 2nd argument) NOT contained in the DataFrame (1st argument), a `ValueError` is thrown. You're now going to play with this function: it is loaded into pre-exercise code, as is the DataFrame `tweets_df`. Try calling `count_entries(tweets_df, 'lang')` to confirm that the function behaves as it should. Then call `count_entries(tweets_df, 'lang1')`: what is the last line of the output?

# ***'ValueError: The DataFrame does not have a lang1 column.'***

# ## Python Data Science Toolbox (Part 2)

# **Course Description**
# 
# In this second course in the Python Data Science Toolbox, you'll continue to build your Python Data Science skills. First you'll enter the wonderful world of iterators, objects that you have already encountered in the context of for loops without having necessarily known it. You'll then learn about list comprehensions, which are extremely handy tools that form a basic component in the toolbox of all modern Data Scientists working in Python. You'll end the course by working through a case study in which you'll apply all of the techniques you learned both in this course as well as the prequel. If you're looking to make it as a Pythonista Data Science ninja, you have come to the right place.

# ### 4 Using iterators in PythonLand
# 
# Here, you'll learn all about iterators and iterables, which you have already worked with before when writing for loops! You'll learn about some very useful functions that will allow you to effectively work with iterators and finish the chapter with a use case that is pertinent to the world of Data Science - dealing with large amounts of data - in this case, data from Twitter that you will load in chunks using iterators!

# ### 4.1 Iterators vs Iterables
# Let's do a quick recall of what you've learned about **iterables** and **iterators**. Recall from the video that an iterable is an object that can return an iterator, while an iterator is an object that keeps state and produces the next value when you call `next()` on it. In this exercise, you will identify which object is an iterable and which is an iterator.
# 
# The environment has been pre-loaded with the variables `flash1` and `flash2`. Try printing out their values with `print()` and `next()` to figure out which is an `iterable` and which is an `iterator`.

# In[41]:


flash1 =  ['jay garrick', 'barry allen', 'wally west', 'bart allen']
flash2 = iter('')


# In[42]:


print(flash1)
print(flash2)


# *Flash1 is an iterable and flash2 is an iterator.*

# ### 4.2 Iterating over iterables (1)
# Great, you're familiar with what iterables and iterators are! In this exercise, you will reinforce your knowledge about these by iterating over and printing from iterables and iterators.
# 
# You are provided with a list of strings `flash`. You will practice iterating over the list by using a `for` loop. You will also create an iterator for the list and access the values from the iterator.
# 
# **Instructions**
# 
# * Create a `for` loop to loop over `flash` and print the values in the list. Use `person` as the loop variable.
# * Create an iterator for the list `flash` and assign the result to `superspeed`.
# * Print each of the items from `superspeed` using `next()` 4 times.

# In[43]:


# Create a list of strings: flash
flash = ['jay garrick', 'barry allen', 'wally west', 'bart allen']

# Print each list item in flash using a for loop
for person in flash:
    print(person)


# Create an iterator for flash: superspeed
superspeed =  iter(flash)

# Print each item from the iterator
print(next(superspeed))
print(next(superspeed))
print(next(superspeed))
print(next(superspeed))


# ### 4.3 Iterating over iterables (2)
# 
# One of the things you learned about in this chapter is that not all iterables are actual lists. A couple of examples that we looked at are strings and the use of the `range()` function. In this exercise, we will focus on the `range()` function.
# 
# You can use `range()` in a `for` loop as if it's a list to be iterated over:
# 
# > ~~~
# > for i in range(5):
#       print(i)
# > ~~~
# 
# 
# Recall that `range()` doesn't actually create the list; instead, it creates a range object with an iterator that produces the values until it reaches the limit (in the example, until the value 4). If `range()` created the actual list, calling it with a value of **10**<sup>**100**</sup> may not work, especially since a number as big as that may go over a regular computer's memory. The value  **10**<sup>**100**</sup> is actually - what's called a **Googol** which is a 1 followed by a hundred 0s. That's a huge number!
# 
# Your task for this exercise is to show that calling `range()` with 10100 won't actually pre-create the list.
# 
# **Instructions**
# 
# - Create an **iterator** object `small_value` over `range(3)` using the function `iter()`.
# - Using a `for` loop, iterate over `range(3)`, printing the value for every iteration. Use `num` as the loop variable.
# - Create an **iterator** object `googol` over `range(10 ** 100)`.
# 

# In[44]:


# Create an iterator for range(3): small_value
small_value = iter(range(3))

# Print the values in small_value
print(next(small_value))
print(next(small_value))
print(next(small_value))

# Loop over range(3) and print the values
for num in range(3):
    print(num)


# Create an iterator for range(10 ** 100): googol
googol = iter(range(10 ** 100))

# Print the first 5 values from googol
print(next(googol))
print(next(googol))
print(next(googol))
print(next(googol))
print(next(googol))


# ### 4.4 Iterators as function arguments
# You've been using the `iter()` function to get an iterator object, as well as the `next()` function to retrieve the values one by one from the iterator object.
# 
# There are also functions that take iterators as arguments. For example, the `list()` and `sum()` functions return a list and the sum of elements, respectively.
# 
# In this exercise, you will use these functions by passing an iterator from `range()` and then printing the results of the function calls.
# 
# **Instructions**
# 
# - Create a `range` object that would produce the values from 10 to 20 using `range()`. Assign the result to `values`.
# - Use the `list()` function to create a list of values from the range object `values`. Assign the result to `values_list`.
# - Use the `sum()` function to get the sum of the values from 10 to 20 from the range object `values`. Assign the result to `values_sum`.

# In[45]:


# Create a range object: values
values = range(10,21)

# Print the range object
print(values)

# Create a list of integers: values_list
values_list = list(values)

# Print values_list
print(values_list)

# Get the sum of values: values_sum
values_sum = sum(values)

# Print values_sum
print(values_sum)


# ### 4.5 Using enumerate
# You're really getting the hang of using iterators, great job!
# 
# You've just gained several new ideas on iterators from the last video and one of them is the `enumerate()` function. Recall that `enumerate()` returns an `enumerate` object that produces a sequence of tuples, and each of the tuples is an index-value pair.
# 
# In this exercise, you are given a list of strings `mutants` and you will practice using `enumerate()` on it by printing out a list of tuples and unpacking the tuples using a `for` loop.
# 
# **Instructions**
# 
# - Create a list of tuples from `mutants` and assign the result to `mutant_list`. Make sure you generate the tuples using `enumerate()` and turn the result from it into a list using `list()`.
# - Complete the first `for` loop by unpacking the tuples generated by calling `enumerate()` on `mutants`. Use `index1` for the index and `value1` for the value when unpacking the tuple.
# - Complete the second `for` loop similarly as with the first, but this time change the starting index to start from `1` by passing it in as an argument to the `star`t parameter of `enumerate()`. Use `index2` for the index and `value2` for the value when unpacking the tuple.

# In[46]:


# Create a list of strings: mutants
mutants = ['charles xavier', 
            'bobby drake', 
            'kurt wagner', 
            'max eisenhardt', 
            'kitty pryde']

# Create a list of tuples: mutant_list
mutant_list = list(enumerate(mutants))

# Print the list of tuples
print(mutant_list)

# Unpack and print the tuple pairs
for index1,value1 in mutant_list:
    print(index1, value1)

# Change the start index
for index2, value2 in enumerate(mutants, start = 1):
    print(index2, value2)


# ### 4.6 Using zip
# Another interesting function that you've learned is `zip()`, which takes any number of iterables and returns a `zip` object that is an iterator of tuples. If you wanted to print the values of a `zip` object, you can convert it into a list and then print it. Printing just a `zip` object will not return the values unless you unpack it first. In this exercise, you will explore this for yourself.
# 
# Three lists of strings are pre-loaded: `mutants`, `aliases`, and `powers`. First, you will use `list()` and `zip()` on these lists to generate a list of tuples. Then, you will create a `zip` object using `zip()`. Finally, you will unpack this `zip` object in a `for` loop to print the values in each tuple. Observe the different output generated by printing the list of tuples, then the `zip` object, and finally, the tuple values in the `for` loop.
# 
# **Instructions**
# 
# - Using `zip()` with `list()`, create a list of tuples from the three lists `mutants`, `aliases`, and `powers` (in that order) and assign the result to `mutant_data`.
# - Using `zip()`, create a `zip` object called `mutant_zip` from the three lists `mutants`, `aliases`, and `powers`.
# - Complete the `for` loop by unpacking the `zip` object you created and printing the tuple values. Use `value1`, `value2`, `value3` for the values from each of `mutants`, `aliases`, and `powers`, in that order.

# In[47]:


aliases = ['prof x', 'iceman', 'nightcrawler', 'magneto', 'shadowcat']
powers = ['telepathy', 'thermokinesis', 'teleportation', 'magnetokinesis', 'intangibility']

# Create a list of tuples: mutant_data
mutant_data = list(zip(mutants, aliases, powers))

# Print the list of tuples
print(mutant_data)

# Create a zip object using the three lists: mutant_zip
mutant_zip = zip(mutants, aliases, powers)

# Print the zip object
print(mutant_zip)

# Unpack the zip object and print the tuple values
for value1, value2, value3 in mutant_zip:
    print(value1, value2, value3)


# ### 4.7 Using * and zip to 'unzip'
# You know how to use `zip()` as well as how to print out values from a `zip` object. Excellent!
# 
# Let's play around with `zip()` a little more. There is no *unzip* function for doing the reverse of what zip() does. We can, however, reverse what has been zipped together by using zip() with a little help from `*` ! `*` unpacks an iterable such as a list or a tuple into *positional arguments* in a function call.
# 
# In this exercise, you will use * in a call to zip() to unpack the tuples produced by zip().
# 
# Two tuples of strings, mutants and powers have been pre-loaded.
# 
# **Instructions** 
# 
# - Create a `zip` object by using `zip()` on `mutants` and `powers`, in that order. Assign the result to `z1`.
# - Print the tuples in `z1` by unpacking them into positional arguments using the `*` operator in a `print()` call.
# - Because the previous `print()` call would have exhausted the elements in `z1`, recreate the `zip` object you defined earlier and assign the result again to `z1`.
# - 'Unzip' the tuples in `z1` by unpacking them into positional arguments using the `*` operator in a `zip()` call. Assign the results to `result1` and `result2`, in that order.
# - The last `print()` statements prints the output of comparing `result1` to `mutants` and `result2` to `powers`. Click `Submit Answe` to see if the unpacked `result1` and `result2` are equivalent to `mutants` and `powers`, respectively.
# 

# In[48]:


# Create a zip object from mutants and powers: z1
z1 = zip(mutants, powers)

# Print the tuples in z1 by unpacking with *
print(*z1)

# Re-create a zip object from mutants and powers: z1
z1 = zip(mutants, powers)

# 'Unzip' the tuples in z1 by unpacking with * and zip(): result1, result2
result1, result2 = zip(*z1)

# Check if unpacked tuples are equivalent to original tuples
print(result1 == mutants)
print(result2 == powers)


# ### 4.8 Processing large amounts of Twitter data
# Sometimes, the data we have to process reaches a size that is too much for a computer's memory to handle. This is a common problem faced by data scientists. A solution to this is to process an entire data source chunk by chunk, instead of a single go all at once.
# 
# In this exercise, you will do just that. You will process a large csv file of Twitter data in the same way that you processed `'tweets.csv'` in Bringing it all together exercises of the prequel course, but this time, working on it in chunks of 10 entries at a time.
# 
# If you are interested in learning how to access Twitter data so you can work with it on your own system, refer to Part 2 of the DataCamp course on Importing Data in Python.
# 
# The pandas package has been imported as `pd` and the file `'tweets.csv'` is in your current directory for your use. Go for it!
# 
# **Instructions**
# 
# - Initialize an empty dictionary `counts_dict` for storing the results of processing the Twitter data.
# - Iterate over the `'tweets.csv'` file by using a `for` loop. Use the loop variable `chunk` and iterate over the call to `pd.read_csv()` with a `chunksize` of 10.
# - In the inner loop, iterate over the column `'lang'` in `chunk` by using a `for` loop. Use the loop variable `entry`.

# In[49]:


import pandas as pd

# Initialize an empty dictionary: counts_dict
counts_dict = {}

# Iterate over the file chunk by chunk
for chunk in pd.read_csv('./Data/tweets.csv', chunksize = 10):

    # Iterate over the column in DataFrame
    for entry in chunk['lang']:
        if entry in counts_dict.keys():
            counts_dict[entry] += 1
        else:
            counts_dict[entry] = 1

# Print the populated dictionary
print(counts_dict)


# ### 4.9 Extracting information for large amounts of Twitter data
# Great job chunking out that file in the previous exercise. You now know how to deal with situations where you need to process a very large file and that's a very useful skill to have!
# 
# It's good to know how to process a file in smaller, more manageable chunks, but it can become very tedious having to write and rewrite the same code for the same task each time. In this exercise, you will be making your code more reusable by putting your work in the last exercise in a function definition.
# 
# The pandas package has been imported as `pd` and the file `'tweets.csv'` is in your current directory for your use.
# 
# **Instructions**
# 
# - Define the function `count_entries()`, which has 3 parameters. The first parameter is `csv_file` for the filename, the second is `c_size` for the chunk size, and the last is `colname` for the column name.
# - Iterate over the file in `csv_file` file by using a `for` loop. Use the loop variable `chunk` and iterate over the call to `pd.read_csv()`, passing `c_size` to `chunksize`.
# - In the inner loop, iterate over the column given by `colname` in `chunk` by using a `for` loop. Use the loop variable `entry`.
# - Call the `count_entries()` function by passing to it the filename `'tweets.csv'`, the size of chunks `10`, and the name of the column to count, `'lang'`. Assign the result of the call to the variable `result_counts`.

# In[50]:


# Define count_entries()
def count_entries(csv_file, c_size, colname):
    """Return a dictionary with counts of
    occurrences as value for each key."""
    
    # Initialize an empty dictionary: counts_dict
    counts_dict = {}

    # Iterate over the file chunk by chunk
    for chunk in pd.read_csv(csv_file, chunksize = c_size):

        # Iterate over the column in DataFrame
        for entry in chunk[colname]:
            if entry in counts_dict.keys():
                counts_dict[entry] += 1
            else:
                counts_dict[entry] = 1

    # Return counts_dict
    return counts_dict

# Call count_entries(): result_counts
result_counts = count_entries('./data/tweets.csv', 10, 'lang')

# Print result_counts
print(result_counts)


# ## 5. List comprehensions and generators
# 
# In this chapter, you'll build on your knowledge of iterators and be introduced to list comprehensions, which allow you to create complicated lists and lists of lists in one line of code! List comprehensions can dramatically simplify your code and make it more efficient, and will become a vital part of your Python Data Science toolbox. You'll then learn about generators, which are extremely helpful when working with large sequences of data that you may not want to store in memory but instead generate on the fly.
# 

# ### 5.1 Write a basic list comprehension
# In this exercise, you will practice what you've learned from the video about writing list comprehensions. You will write a list comprehension and identify the output that will be produced.
# 
# The following list has been pre-loaded in the environment.
# ~~~
# doctor = ['house', 'cuddy', 'chase', 'thirteen', 'wilson']
# ~~~
# How would a list comprehension that produces a list of the **first character** of each string in `doctor` look like? Note that the list comprehension uses `doc` as the iterator variable. What will the output be?
# 
# **Instructions**
# 
# Answers
# 
# The list comprehension is [doc[0] for doc in doctor] and produces the list ['h', 'c', 'c', 't', 'w'].

# In[51]:


doctor = ['house', 'cuddy', 'chase', 'thirteen', 'wilson']

[doc[0] for doc in doctor]


# ### 5.2 List comprehension over iterables
# You know that list comprehensions can be built over iterables. Given the following objects below, which of these can we build list comprehensions over?
# ~~~
# doctor = ['house', 'cuddy', 'chase', 'thirteen', 'wilson']
# 
# range(50)
# 
# underwood = 'After all, we are nothing more or less than what we choose to reveal.'
# 
# jean = '24601'
# 
# flash = ['jay garrick', 'barry allen', 'wally west', 'bart allen']
# 
# valjean = 24601
# ~~~
# **Instructions**
# 
# Possible Answers
# 
# - You can build list comprehensions over all the objects except the string of number characters `jean`.
# - You can build list comprehensions over all the objects except the string lists `doctor` and `flash`.
# - You can build list comprehensions over all the objects except `range(50)`.
# - **You can build list comprehensions over all the objects except the integer object `valjean`.**

# ### 5.3 Writing list comprehensions
# You now have all the knowledge necessary to begin writing list comprehensions! Your job in this exercise is to write a list comprehension that produces a list of the squares of the numbers ranging from 0 to 9.
# 
# **Instructions**
# 
# - Using the range of numbers from `0` to `9` as your iterable and `i` as your iterator variable, write a list comprehension that produces a list of numbers consisting of the squared values of `i`.

# In[52]:


# Create list comprehension: squares
squares = [i**2 for i in range(0,10)]
print(squares)


# ### 5.3 Nested list comprehensions
# Great! At this point, you have a good grasp of the basic syntax of list comprehensions. Let's push your code-writing skills a little further. In this exercise, you will be writing a list comprehension within another list comprehension, or nested list comprehensions. It sounds a little tricky, but you can do it!
# 
# Let's step aside for a while from strings. One of the ways in which lists can be used are in representing multi-dimension objects such as matrices. Matrices can be represented as a list of lists in Python. For example a 5 x 5 matrix with values 0 to 4 in each row can be written as:
# ~~~
# matrix = [[0, 1, 2, 3, 4],
#           [0, 1, 2, 3, 4],
#           [0, 1, 2, 3, 4],
#           [0, 1, 2, 3, 4],
#           [0, 1, 2, 3, 4]]
# ~~~          
# Your task is to recreate this matrix by using nested listed comprehensions. Recall that you can create one of the rows of the matrix with a single list comprehension. To create the list of lists, you simply have to supply the list comprehension as the **output expression** of the overall list comprehension:
# 
# `[`[*output expression*] `for` *iterator variable* `in` *iterable*`]`
# 
# Note that here, the *output expression* is itself a list comprehension.
# 
# **Instructions**
# 
# - In the inner list comprehension - that is, the **output expression** of the nested list comprehension - create a list of values from `0` to `4` using `range()`. Use `col` as the iterator variable.
# - In the iterable part of your nested list comprehension, use `range()` to count 5 rows - that is, create a list of values from `0` to `4`. Use `row` as the iterator variable; note that you won't be needing this to create values in the list of lists.

# In[53]:


# Create a 5 x 5 matrix using a list of lists: matrix
matrix = [[col for col in range(5)] for row in range(5)]

# Print the matrix
for row in matrix:
    print(row)


# ### 5.4 Using conditionals in comprehensions (1)
# You've been using list comprehensions to build lists of values, sometimes using operations to create these values.
# 
# An interesting mechanism in list comprehensions is that you can also create lists with values that meet only a certain condition. One way of doing this is by using conditionals on iterator variables. In this exercise, you will do exactly that!
# 
# Recall from the video that you can apply a conditional statement to test the iterator variable by adding an `if` statement in the optional predicate expression part after the `for` statement in the comprehension:
# 
# `[` *output expression* `for` *iterator variable* `in` *iterable* `if` *predicate expression* `]`.
# 
# You will use this recipe to write a list comprehension for this exercise. You are given a list of strings `fellowship` and, using a list comprehension, you will create a list that only includes the members of `fellowship` that have 7 characters or more.
# 
# **Instructions**
# 
# - Use `member` as the iterator variable in the list comprehension. For the conditional, use `len()` to evaluate the iterator variable. Note that you only want strings with 7 characters or more.

# In[54]:


# Create a list of strings: fellowship
fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']

# Create list comprehension: new_fellowship
new_fellowship = [member for member in fellowship if len(member) >= 7]

# Print the new list
print(new_fellowship)


# ### 5.5 Using conditionals in comprehensions (2)
# In the previous exercise, you used an `if` conditional statement in the predicate expression part of a list comprehension to evaluate an iterator variable. In this exercise, you will use an `if-else` statement on the output expression of the list.
# 
# You will work on the same list, `fellowship` and, using a list comprehension and an `if-else` conditional statement in the output expression, create a list that keeps members of `fellowship` with 7 or more characters and replaces others with an empty string. Use `member` as the iterator variable in the list comprehension.
# 
# **Instructions**
# 
# - In the output expression, keep the string as-is **if** the number of characters is >= 7, **else** replace it with an *empty string* - that is, `''` or `""`.

# In[55]:


# Create a list of strings: fellowship
fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']

# Create list comprehension: new_fellowship
new_fellowship = [member if len(member) >= 7 else '' for member in fellowship]

# Print the new list
print(new_fellowship)


# ### 5.6 Dict comprehensions
# Comprehensions aren't relegated merely to the world of lists. There are many other objects you can build using comprehensions, such as dictionaries, pervasive objects in Data Science. You will create a dictionary using the comprehension syntax for this exercise. In this case, the comprehension is called a **dict comprehension**.
# 
# Recall that the main difference between a list comprehension and a dict comprehension is the use of curly braces `{}` instead of `[]`. Additionally, members of the dictionary are created using a colon `:`, as in `<key> : <value>`.
# 
# You are given a list of strings `fellowship` and, using a **dict comprehension**, create a dictionary with the members of the list as the keys and the length of each string as the corresponding values.
# 
# **Instructions**
# 
# - Create a dict comprehension where the key is a string in `fellowship` and the value is the length of the string. Remember to use the syntax `<key> : <value>` in the output expression part of the comprehension to create the members of the dictionary. Use `member` as the iterator variable.

# In[56]:


# Create a list of strings: fellowship
fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']

# Create dict comprehension: new_fellowship
new_fellowship = {member : len(member) for member in fellowship}

# Print the new list
print(new_fellowship)


# ### 5.7 List comprehensions vs generators
# You've seen from the videos that list comprehensions and generator expressions look very similar in their syntax, except for the use of parentheses `()` in generator expressions and brackets `[]`in list comprehensions.
# 
# In this exercise, you will recall the difference between list comprehensions and generators. To help with that task, the following code has been pre-loaded in the environment:
# ~~~
# # List of strings
# fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']
# 
# # List comprehension
# fellow1 = [member for member in fellowship if len(member) >= 7]
# 
# # Generator expression
# 
# fellow2 = (member for member in fellowship if len(member) >= 7)
# ~~~
# Try to play around with `fellow1` and `fellow2` by figuring out their types and printing out their values. Based on your observations and what you can recall from the video, select from the options below the best description for the difference between list comprehensions and generators.
# 
# **Instructions**
# 
# Possible Answers
# - List comprehensions and generators are not different at all; they are just different ways of writing the same thing.
# - **A list comprehension produces a list as output, a generator produces a generator object.**
# - A list comprehension produces a list as output that can be iterated over, a generator produces a generator object that can't be iterated over.

# ### 5.8 Write your own generator expressions
# You are familiar with what generators and generator expressions are, as well as its difference from list comprehensions. In this exercise, you will practice building generator expressions on your own.
# 
# Recall that generator expressions basically have the same syntax as list comprehensions, except that it uses parentheses `()` instead of brackets `[]`; this should make things feel familiar! Furthermore, if you have ever iterated over a dictionary with `.items()`, or used the `range()` function, for example, you have already encountered and used generators before, without knowing it! When you use these functions, Python creates generators for you behind the scenes.
# 
# Now, you will start simple by creating a generator object that produces numeric values.
# 
# **Instructions**
# 
# - Create a generator object that will produce values from `0` to `30`. Assign the result to `result` and use `num` as the iterator variable in the generator expression.
# - Print the first `5` values by using `next()` appropriately in `print()`.
# - Print the rest of the values by using a `for` loop to iterate over the generator object.

# In[57]:


# Create generator object: result
result = (num for num in range(0,31))

# Print the first 5 values
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))

# Print the rest of the values
for value in result:
    print(value)


# ### 5.9 Changing the output in generator expressions
# Great! At this point, you already know how to write a basic generator expression. In this exercise, you will push this idea a little further by adding to the output expression of a generator expression. Because generator expressions and list comprehensions are so alike in syntax, this should be a familiar task for you!
# 
# You are given a list of strings `lannister` and, using a generator expression, create a generator object that you will iterate over to print its values.
# 
# **Instructions**
# 
# - Write a generator expression that will generate the lengths of each string in `lannister`. Use `person` as the iterator variable. Assign the result to `lengths`.
# - Supply the correct iterable in the `for` loop for printing the values in the generator object.

# In[58]:


# Create a list of strings: lannister
lannister = ['cersei', 'jaime', 'tywin', 'tyrion', 'joffrey']

# Create a generator object: lengths
lengths = (len(person) for person in lannister)

# Iterate over and print the values in lengths
for value in lengths:
    print(value)


# ### 5.10 Build a generator
# In previous exercises, you've dealt mainly with writing generator expressions, which uses comprehension syntax. Being able to use comprehension syntax for generator expressions made your work so much easier!
# 
# Now, recall from the video that not only are there generator expressions, there are generator functions as well. **Generator functions** are functions that, like generator expressions, yield a series of values, instead of returning a single value. A generator function is defined as you do a regular function, but whenever it generates a value, it uses the keyword `yield` instead of `return`.
# 
# In this exercise, you will create a generator function with a similar mechanism as the generator expression you defined in the previous exercise:
# ~~~
# lengths = (len(person) for person in lannister)
# ~~~
# **Instructions**
# 
# - Complete the function header for the function `get_lengths()` that has a single parameter, `input_list`.
# - In the `for` loop in the function definition, `yield` the length of the strings in `input_list`.
# - Complete the iterable part of the `for` loop for printing the values generated by the `get_lengths()` generator function. Supply the call to `get_lengths()`, passing in the list `lannister`.

# In[59]:


# Create a list of strings
lannister = ['cersei', 'jaime', 'tywin', 'tyrion', 'joffrey']

# Define generator function get_lengths
def get_lengths(input_list):
    """Generator function that yields the
    length of the strings in input_list."""

    # Yield the length of a string
    for person in input_list:
        yield len(person)

# Print the values generated by get_lengths()
for value in get_lengths(lannister):
    print(value)


# ### 5.11 List comprehensions for time-stamped data
# You will now make use of what you've learned from this chapter to solve a simple data extraction problem. You will also be introduced to a data structure, the pandas **Series**, in this exercise. We won't elaborate on it much here, but what you should know is that it is a data structure that you will be working with a lot of times when analyzing data from pandas DataFrames. You can think of DataFrame columns as single-dimension arrays called Series.
# 
# In this exercise, you will be using a list comprehension to extract the time from time-stamped Twitter data. The pandas package has been imported as `pd` and the file `'tweets.csv'` has been imported as the `df` DataFrame for your use.
# 
# **Instructions**
# 
# - Extract the column `'created_at'` from `df` and assign the result to `tweet_time`. Fun fact: the extracted column in `tweet_time` here is a Series data structure!
# - Create a list comprehension that extracts the time from each row in `tweet_time`. Each row is a string that represents a timestamp, and you will access the 12th to 19th characters in the string to extract the time. Use `entry` as the iterator variable and assign the result to `tweet_clock_time`. Remember that Python uses 0-based indexing!

# In[60]:


import pandas as pd
df = pd.read_csv('Data/tweets.csv')

# Extract the created_at column from df: tweet_time
tweet_time = df['created_at']

# Extract the clock time: tweet_clock_time
tweet_clock_time = [entry[11:19] for entry in tweet_time]

# Print the extracted times
print(tweet_clock_time)


# ### 5.12 Conditional list comprehensions for time-stamped data
# Great, you've successfully extracted the data of interest, the time, from a pandas DataFrame! Let's tweak your work further by adding a conditional that further specifies which entries to select.
# 
# In this exercise, you will be using a list comprehension to extract the time from time-stamped Twitter data. You will add a conditional expression to the list comprehension so that you only select the times in which `entry[17:19]` is equal to `'19'`. The pandas package has been imported as `pd` and the file `'tweets.csv'` has been imported as the `df` DataFrame for your use.
# 
# **Instructions**
# 
# - Extract the column `'created_at'` from `df` and assign the result to `tweet_time`.
# - Create a list comprehension that extracts the time from each row in `tweet_time`. Each row is a string that represents a timestamp, and you will access the 12th to 19th characters in the string to extract the time. Use `entry` as the iterator variable and assign the result to `tweet_clock_time`. Additionally, add a conditional expression that checks whether `entry[17:19]` is equal to `'19'`

# In[61]:


# Extract the created_at column from df: tweet_time
tweet_time = df['created_at']

# Extract the clock time: tweet_clock_time
tweet_clock_time = [entry[11:19] for entry in tweet_time if entry[17:19] == '19']

# Print the extracted times
print(tweet_clock_time)


# ### 6. Bringing it all together!
# 
# This chapter will allow you to apply your newly acquired skills towards wrangling and extracting meaningful information from a real-world dataset - the World Bank's World Development Indicators dataset! You'll have the chance to write your own functions and list comprehensions as you work with iterators and generators and solidify your Python Data Science chops. Enjoy!

# ### 6.1 Dictionaries for data science
# For this exercise, you'll use what you've learned about the `zip()` function and combine two lists into a dictionary.
# 
# These lists are actually extracted from a bigger dataset file of world development indicators from the World Bank. For pedagogical purposes, we have pre-processed this dataset into the lists that you'll be working with.
# 
# The first list `feature_names` contains header names of the dataset and the second list `row_vals` contains actual values of a row from the dataset, corresponding to each of the header names.
# 
# **Instructions**
# 
# - Create a zip object by calling `zip()` and passing to it `feature_names` and `row_vals`. Assign the result to `zipped_lists`.
# - Create a dictionary from the `zipped_lists` zip object by calling `dict()` with `zipped_lists`. Assign the resulting dictionary to `rs_dict`.
# 

# In[62]:


feature_names = ['CountryName', 'CountryCode', 'IndicatorName'
                 , 'IndicatorCode', 'Year', 'Value']
row_vals = ['Arab World', 'ARB', 
            'Adolescent fertility rate (births per 1,000 women ages 15-19)',
            'SP.ADO.TFRT', '1960', '133.56090740552298']

# Zip lists: zipped_lists
zipped_lists = zip(feature_names, row_vals)

# Create a dictionary: rs_dict
rs_dict = dict(zipped_lists)

# Print the dictionary
print(rs_dict)


# ### 6.2 Writing a function to help you
# Suppose you needed to repeat the same process done in the previous exercise to many, many rows of data. Rewriting your code again and again could become very tedious, repetitive, and unmaintainable.
# 
# In this exercise, you will create a function to house the code you wrote earlier to make things easier and much more concise. Why? This way, you only need to call the function and supply the appropriate lists to create your dictionaries! Again, the lists `feature_names` and `row_vals` are preloaded and these contain the header names of the dataset and actual values of a row from the dataset, respectively.
# 
# **Instructions**
# 
# - Define the function `lists2dict()` with two parameters: first is `list1` and second is `list2`.
# - Return the resulting dictionary `rs_dict` in `lists2dict()`.
# - Call the `lists2dict()` function with the arguments `feature_names` and `row_vals`. Assign the result of the function call to `rs_fxn`.

# In[63]:


# Define lists2dict()
def lists2dict(list1, list2):
    """Return a dictionary where list1 provides
    the keys and list2 provides the values."""

    # Zip lists: zipped_lists
    zipped_lists = zip(list1, list2)

    # Create a dictionary: rs_dict
    rs_dict = dict(zipped_lists)

    # Return the dictionary
    return rs_dict

# Call lists2dict: rs_fxn
rs_fxn = lists2dict(feature_names, row_vals)

# Print rs_fxn
print(rs_fxn)


# ### 6.3 Using a list comprehension
# This time, you're going to use the `lists2dict()` function you defined in the last exercise to turn a bunch of lists into a list of dictionaries with the help of a list comprehension.
# 
# The `lists2dict()` function has already been preloaded, together with a couple of lists, `feature_names` and `row_lists`. `feature_names` contains the header names of the World Bank dataset and `row_lists` is a list of lists, where each sublist is a list of actual values of a row from the dataset.
# 
# Your goal is to use a list comprehension to generate a list of dicts, where the keys are the header names and the values are the row entries.
# 
# **Instructions**
# 
# - Inspect the contents of `row_lists` by printing the first two lists in `row_lists`.
# - Create a list comprehension that generates a dictionary using `lists2dict()` for each sublist in `row_lists`. The keys are from the `feature_names` list and the values are the row entries in `row_lists`. Use `sublist` as your iterator variable and assign the resulting list of dictionaries to `list_of_dicts`.
# - Look at the first two dictionaries in `list_of_dicts` by printing them out.

# In[64]:


row_lists = [['Arab World',
  'ARB', 'Adolescent fertility rate (births per 1,000 women ages 15-19)',
  'SP.ADO.TFRT', '1960',
  '133.56090740552298'],
 ['Arab World',  'ARB',
  'Age dependency ratio (% of working-age population)',
  'SP.POP.DPND',  '1960',
  '87.7976011532547'],
 ['Arab World',  'ARB',
  'Age dependency ratio, old (% of working-age population)',
  'SP.POP.DPND.OL',  '1960',
  '6.634579191565161'],
 ['Arab World',
  'ARB',
  'Age dependency ratio, young (% of working-age population)',
  'SP.POP.DPND.YG',
  '1960',
  '81.02332950839141'],
 ['Arab World',
  'ARB',
  'Arms exports (SIPRI trend indicator values)',
  'MS.MIL.XPRT.KD',
  '1960',
  '3000000.0'],
 ['Arab World',
  'ARB',
  'Arms imports (SIPRI trend indicator values)',
  'MS.MIL.MPRT.KD',
  '1960',
  '538000000.0'],
 ['Arab World',
  'ARB',
  'Birth rate, crude (per 1,000 people)',
  'SP.DYN.CBRT.IN',
  '1960',
  '47.697888095096395'],
 ['Arab World',
  'ARB',
  'CO2 emissions (kt)',
  'EN.ATM.CO2E.KT',
  '1960',
  '59563.9892169935'],
 ['Arab World',
  'ARB',
  'CO2 emissions (metric tons per capita)',
  'EN.ATM.CO2E.PC',
  '1960',
  '0.6439635478877049'],
 ['Arab World',
  'ARB',
  'CO2 emissions from gaseous fuel consumption (% of total)',
  'EN.ATM.CO2E.GF.ZS',
  '1960',
  '5.041291753975099'],
 ['Arab World',
  'ARB',
  'CO2 emissions from liquid fuel consumption (% of total)',
  'EN.ATM.CO2E.LF.ZS',
  '1960',
  '84.8514729446567'],
 ['Arab World',
  'ARB',
  'CO2 emissions from liquid fuel consumption (kt)',
  'EN.ATM.CO2E.LF.KT',
  '1960',
  '49541.707291032304'],
 ['Arab World',
  'ARB',
  'CO2 emissions from solid fuel consumption (% of total)',
  'EN.ATM.CO2E.SF.ZS',
  '1960',
  '4.72698138789597'],
 ['Arab World',
  'ARB',
  'Death rate, crude (per 1,000 people)',
  'SP.DYN.CDRT.IN',
  '1960',
  '19.7544519237187'],
 ['Arab World',
  'ARB',
  'Fertility rate, total (births per woman)',
  'SP.DYN.TFRT.IN',
  '1960',
  '6.92402738655897'],
 ['Arab World',
  'ARB',
  'Fixed telephone subscriptions',
  'IT.MLT.MAIN',
  '1960',
  '406833.0'],
 ['Arab World',
  'ARB',
  'Fixed telephone subscriptions (per 100 people)',
  'IT.MLT.MAIN.P2',
  '1960',
  '0.6167005703199'],
 ['Arab World',
  'ARB',
  'Hospital beds (per 1,000 people)',
  'SH.MED.BEDS.ZS',
  '1960',
  '1.9296220724398703'],
 ['Arab World',
  'ARB',
  'International migrant stock (% of population)',
  'SM.POP.TOTL.ZS',
  '1960',
  '2.9906371279862403'],
 ['Arab World',
  'ARB',
  'International migrant stock, total',
  'SM.POP.TOTL',
  '1960',
  '3324685.0']]


# In[65]:


# Print the first two lists in row_lists
print(row_lists[0])
print(row_lists[1])

# Turn list of lists into list of dicts: list_of_dicts
list_of_dicts = [lists2dict(feature_names, sublist) for sublist in row_lists]

# Print the first two dictionaries in list_of_dicts
print(list_of_dicts[0])
print(list_of_dicts[1])


# ### 6.4 Turning this all into a DataFrame
# You've zipped lists together, created a function to house your code, and even used the function in a list comprehension to generate a list of dictionaries. That was a lot of work and you did a great job!
# 
# You will now use of all these to convert the list of dictionaries into a pandas DataFrame. You will see how convenient it is to generate a DataFrame from dictionaries with the `DataFrame()` function from the pandas package.
# 
# The `lists2dict()` function, feature_names list, and `row_lists` list have been preloaded for this exercise.
# 
# Go for it!
# 
# **Instructions**
# 
# - To use the `DataFrame()` function you need, first import the pandas package with the alias `pd`.
# - Create a DataFrame from the list of dictionaries in `list_of_dicts` by calling `pd.DataFrame()`. Assign the resulting DataFrame to `df`.
# - Inspect the contents of `df` by printing the head of the DataFrame.

# In[66]:


# Import the pandas package
import pandas as pd

# Turn list of lists into list of dicts: list_of_dicts
list_of_dicts = [lists2dict(feature_names, sublist) for sublist in row_lists]

# Turn list of dicts into a DataFrame: df
df = pd.DataFrame(list_of_dicts)

# Print the head of the DataFrame
print(df.head())


# ### 6.5 Processing data in chunks (1)
# Sometimes, data sources can be so large in size that storing the entire dataset in memory becomes too resource-intensive. In this exercise, you will process the first 1000 rows of a file line by line, to create a dictionary of the counts of how many times each country appears in a column in the dataset.
# 
# The csv file `'world_dev_ind.csv'` is in your current directory for your use. To begin, you need to open a connection to this file using what is known as a context manager. For example, the command with 
# ~~~
# open('datacamp.csv') as datacamp 
# ~~~
# binds the csv file `'datacamp.csv'` as `datacamp` in the context manager. Here, the `with` statement is the context manager, and its purpose is to ensure that resources are efficiently allocated when opening a connection to a file.
# 
# If you'd like to learn more about context managers, refer to the DataCamp course on Importing Data in Python.
# 
# **Instructions**
# 
# - Use `open()` to bind the csv file `'world_dev_ind.csv'` as `file` in the context manager.
# - Complete the `for` loop so that it iterates **1000** times to perform the loop body and process only the first 1000 rows of data of the file.

# In[67]:


# Open a connection to the file
with open ('./Data/world_dev_ind.csv') as file:

    # Skip the column names
    file.readline()

    # Initialize an empty dictionary: counts_dict
    counts_dict = {}

    # Process only the first 1000 rows
    for j in range(0, 1000):

        # Split the current line into a list: line
        line = file.readline().split(',')

        # Get the value for the first column: first_col
        first_col = line[0]

        # If the column value is in the dict, increment its value
        if first_col in counts_dict.keys():
            counts_dict[first_col] += 1

        # Else, add to the dict and set value to 1
        else:
            counts_dict[first_col] = 1

# Print the resulting dictionary
print(counts_dict)


# ### 6.6 Writing a generator to load data in chunks (2)
# In the previous exercise, you processed a file line by line for a given number of lines. What if, however, you want to do this for the entire file?
# 
# In this case, it would be useful to use **generators**. Generators allow users to lazily evaluate data. This concept of lazy evaluation is useful when you have to deal with very large datasets because it lets you generate values in an efficient manner by yielding only chunks of data at a time instead of the whole thing at once.
# 
# In this exercise, you will define a generator function `read_large_file()` that produces a generator object which yields a single line from a file each time `next()` is called on it. The csv file `'world_dev_ind.csv'` is in your current directory for your use.
# 
# Note that when you open a connection to a file, the resulting file object is already a generator! So out in the wild, you won't have to explicitly create generator objects in cases such as this. However, for pedagogical reasons, we are having you practice how to do this here with the `read_large_file()` function. Go for it!
# 
# **Instructions**
# 
# - In the function `read_large_file()`, read a line from `file_object` by using the method `readline()`. Assign the result to `data`.
# - In the function `read_large_file()`, `yield` the line read from the file `data`.
# - In the context manager, create a generator object `gen_file` by calling your generator function `read_large_file()` and passing `file` to it.
# - Print the first three lines produced by the generator object `gen_file` using `next()`.

# In[68]:


# Define read_large_file()
def read_large_file(file_object):
    """A generator function to read a large file lazily."""

    # Loop indefinitely until the end of the file
    while True:

        # Read a line from the file: data
        data = file_object.readline()

        # Break if this is the end of the file
        if not data:
            break

        # Yield the line of data
        yield data
        
# Open a connection to the file
with open('./Data/world_dev_ind.csv') as file:

    # Create a generator object for the file: gen_file
    gen_file = read_large_file(file)

    # Print the first three lines of the file
    print(next(gen_file))
    print(next(gen_file))
    print(next(gen_file))


# ### 6.7 Writing a generator to load data in chunks (3)
# Great! You've just created a generator function that you can use to help you process large files.
# 
# Now let's use your generator function to process the World Bank dataset like you did previously. You will process the file line by line, to create a dictionary of the counts of how many times each country appears in a column in the dataset. For this exercise, however, you won't process just 1000 rows of data, you'll process the entire dataset!
# 
# The generator function `read_large_file()` and the csv file `'world_dev_ind.csv'` are preloaded and ready for your use. Go for it!
# 
# **Instructions**
# 
# - Bind the file `'world_dev_ind.csv'` to `file` in the context manager with `open()`.
# - Complete the `for` loop so that it iterates over the generator from the call to `read_large_file()` to process all the rows of the file.
# 

# In[69]:


# Initialize an empty dictionary: counts_dict
counts_dict = {}

# Open a connection to the file
with open ('./Data/world_dev_ind.csv') as file:

    # Iterate over the generator from read_large_file()
    for line in read_large_file(file):

        row = line.split(',')
        first_col = row[0]

        if first_col in counts_dict.keys():
            counts_dict[first_col] += 1
        else:
            counts_dict[first_col] = 1

# Print            
print(counts_dict)


# ### 6.8 Writing an iterator to load data in chunks (1)
# Another way to read data too large to store in memory in chunks is to read the file in as DataFrames of a certain length, say, 100. For example, with the pandas package (imported as `pd`), you can do 
# ~~~
# pd.read_csv(filename, chunksize=100)
# ~~~
# . This creates an **iterable reader** object, which means that you can use `next()` on it.
# 
# In this exercise, you will read a file in small DataFrame chunks with `read_csv()`. You're going to use the World Bank Indicators data `'ind_pop.csv'`, available in your current directory, to look at the urban population indicator for numerous countries and years.
# 
# **Instructions**
# 
# - Use `pd.read_csv()` to read in `'ind_pop.csv'` in chunks of size 10. Assign the result to `df_reader.
# - Print the first two chunks from `df_reader`.

# In[70]:


# Import the pandas package
import pandas as pd

# Initialize reader object: df_reader
df_reader = pd.read_csv('./Data/world_dev_ind.csv', chunksize=10)

# Print two chunks
print(next(df_reader))
print(next(df_reader))


# ### 6.9 Writing an iterator to load data in chunks (2)
# In the previous exercise, you used `read_csv()` to read in DataFrame chunks from a large dataset. In this exercise, you will read in a file using a bigger DataFrame chunk size and then process the data from the first chunk.
# 
# To process the data, you will create another DataFrame composed of only the rows from a specific country. You will then zip together two of the columns from the new DataFrame, `'Total Population'` and `'Urban population (% of total)'`. Finally, you will create a list of tuples from the zip object, where each tuple is composed of a value from each of the two columns mentioned.
# 
# You're going to use the data from `'ind_pop_data.csv'`, available in your current directory. Pandas has been imported as pd.
# 
# **Instructions**
# 
# - Use `pd.read_csv()` to read in the file in `'ind_pop_data.csv'` in chunks of size `1000`. Assign the result to `urb_pop_reader`.
# - Get the first DataFrame chunk from the iterable `urb_pop_reader` and assign this to `df_urb_pop`.
# - Select only the rows of `df_urb_pop` that have a `'CountryCode'` of `'CEB'`. To do this, compare whether `df_urb_pop['CountryCode']` is equal to `'CEB'` within the square brackets in `df_urb_pop[____]`.
# - Using `zip()`, zip together the `'Total Population'` and `'Urban population (% of total)'` columns of `df_pop_ceb`. Assign the resulting zip object to `pops`.

# In[71]:


# Initialize reader object: urb_pop_reader
urb_pop_reader = pd.read_csv('./Data/world_dev_ind.csv', chunksize = 1000)

# Get the first DataFrame chunk: df_urb_pop
df_urb_pop = next(urb_pop_reader)

# Check out the head of the DataFrame
print(df_urb_pop.head())

# Check out specific country: df_pop_ceb
df_pop_ceb = df_urb_pop[df_urb_pop['CountryCode'] == 'CEB']

# Zip DataFrame columns of interest: pops
pops = zip(df_pop_ceb['Total Population'], df_pop_ceb['Urban population (% of total)'])

# Turn zip object into list: pops_list
pops_list = list(pops)

# Print pops_list
print(pops_list)


# ### 6.10 Writing an iterator to load data in chunks (3)
# You're getting used to reading and processing data in chunks by now. Let's push your skills a little further by adding a column to a DataFrame.
# 
# Starting from the code of the previous exercise, you will be using a list comprehension to create the values for a new column `'Total Urban Population'` from the list of tuples that you generated earlier. Recall from the previous exercise that the first and second elements of each tuple consist of, respectively, values from the columns `'Total Population'` and `'Urban population (% of total)'`. The values in this new column `'Total Urban Population'`, therefore, are the product of the first and second element in each tuple. Furthermore, because the 2nd element is a percentage, you need to divide the entire result by `100`, or alternatively, multiply it by `0.01`.
# 
# You will also plot the data from this new column to create a visualization of the urban population data.
# 
# The packages `pandas` and `matplotlib.pyplot` have been imported as `pd` and `plt` respectively for your use.
# 
# **Instructions**
# 
# - Write a list comprehension to generate a list of values from `pops_list` for the new column `'Total Urban Population'`. The output expression should be the product of the first and second element in each tuple in `pops_list`. Because the 2nd element is a percentage, you also need to either multiply the result by `0.01` or divide it by `100`. In addition, note that the column `'Total Urban Population'` should only be able to take on integer values. To ensure this, make sure you cast the output expression to an integer with `int()`.
# - Create a scatter plot where the x-axis are values from the `'Year'` column and the y-axis are values from the `'Total Urban Population'` column.

# In[72]:


import pandas as pd
# Code from previous exercise
urb_pop_reader = pd.read_csv('./Data/world_dev_ind.csv', chunksize=1000)
df_urb_pop = next(urb_pop_reader)
df_pop_ceb = df_urb_pop[df_urb_pop['CountryCode'] == 'CEB']
pops = zip(df_pop_ceb['Total Population'], 
           df_pop_ceb['Urban population (% of total)'])
pops_list = list(pops)

# Use list comprehension to create new DataFrame column 'Total Urban Population'
df_pop_ceb['Total Urban Population'] = [int(pop[0]* pop[1]/100) for pop in pops_list]

# Plot urban population data
df_pop_ceb.plot(kind='scatter' , x='Year', y='Total Urban Population')
#plt.show()


# ### 6.11 Writing an iterator to load data in chunks (4)
# In the previous exercises, you've only processed the data from the first DataFrame chunk. This time, you will aggregate the results over all the DataFrame chunks in the dataset. This basically means you will be processing the entire dataset now. This is neat because you're going to be able to process the entire large dataset by just working on smaller pieces of it!
# 
# You're going to use the data from `'ind_pop_data.csv'`, available in your current directory. The packages `pandas` and `matplotlib.pyplot` have been imported as pd and plt respectively for your use.
# 
# **Instructions**
# 
# - Initialize an empty DataFrame `data` using `pd.DataFrame()`.
# - In the `for` loop, iterate over `urb_pop_reader` to be able to process all the DataFrame chunks in the dataset.
# - Using `append()` on `data`, append `df_pop_ceb` to `data`.

# In[73]:


# Initialize reader object: urb_pop_reader
urb_pop_reader = pd.read_csv('./Data/world_dev_ind.csv', chunksize=1000)

# Initialize empty DataFrame: data
data = pd.DataFrame()

# Iterate over each DataFrame chunk
for df_urb_pop in urb_pop_reader:

    # Check out specific country: df_pop_ceb
    df_pop_ceb = df_urb_pop[df_urb_pop['CountryCode'] == 'CEB']

    # Zip DataFrame columns of interest: pops
    pops = zip(df_pop_ceb['Total Population'],
                df_pop_ceb['Urban population (% of total)'])

    # Turn zip object into list: pops_list
    pops_list = list(pops)

    # Use list comprehension to create new DataFrame column 'Total Urban Population'
    df_pop_ceb['Total Urban Population'] = [int(tup[0] * tup[1] * 0.01) for tup in pops_list]
    
    # Append DataFrame chunk to data: data
    data = data.append(df_pop_ceb)

# Plot urban population data
data.plot(kind='scatter', x='Year', y='Total Urban Population')
#plt.show()


# ### 6.12 Writing an iterator to load data in chunks (5)
# This is the last leg. You've learned a lot about processing a large dataset in chunks. In this last exercise, you will put all the code for processing the data into a single function so that you can reuse the code without having to rewrite the same things all over again.
# 
# You're going to define the function `plot_pop()` which takes two arguments: the filename of the file to be processed, and the country code of the rows you want to process in the dataset.
# 
# Because all of the previous code you've written in the previous exercises will be housed in `plot_pop()`, calling the function already does the following:
# 
# Loading of the file chunk by chunk,
# Creating the new column of urban population values, and
# Plotting the urban population data.
# That's a lot of work, but the function now makes it convenient to repeat the same process for whatever file and country code you want to process and visualize!
# 
# You're going to use the data from `'ind_pop_data.csv'`, available in your current directory. The packages pandas and matplotlib.pyplot has been imported as `pd` and `plt` respectively for your use.
# 
# After you are done, take a moment to look at the plots and reflect on the new skills you have acquired. The journey doesn't end here! If you have enjoyed working with this data, you can continue exploring it using the pre-processed version available on Kaggle.
# 
# **Instructions**
# 
# - Define the function `plot_pop()` that has two arguments: first is `filename` for the file to process and second is `country_code` for the country to be processed in the dataset.
# - Call `plot_pop()` to process the data for country code `'CEB'` in the file `'ind_pop_data.csv'`.
# - Call `plot_pop()` to process the data for country code `'ARB'` in the file `'ind_pop_data.csv'`.

# In[74]:


# Define plot_pop()
def plot_pop(filename, country_code):

    # Initialize reader object: urb_pop_reader
    urb_pop_reader = pd.read_csv(filename, chunksize=1000)

    # Initialize empty DataFrame: data
    data = pd.DataFrame()
    
    # Iterate over each DataFrame chunk
    for df_urb_pop in urb_pop_reader:
        # Check out specific country: df_pop_ceb
        df_pop_ceb = df_urb_pop[df_urb_pop['CountryCode'] == country_code]

        # Zip DataFrame columns of interest: pops
        pops = zip(df_pop_ceb['Total Population'],
                    df_pop_ceb['Urban population (% of total)'])

        # Turn zip object into list: pops_list
        pops_list = list(pops)

        # Use list comprehension to create new DataFrame column 'Total Urban Population'
        df_pop_ceb['Total Urban Population'] = [int(tup[0] * tup[1] * 0.01) for tup in pops_list]
    
        # Append DataFrame chunk to data: data
        data = data.append(df_pop_ceb)

    # Plot urban population data
    data.plot(kind='scatter', x='Year', y='Total Urban Population')
    #plt.show()

# Set the filename: fn
fn = './Data/world_dev_ind.csv'

# Call plot_pop for country code 'CEB'
plot_pop(fn, 'CEB')

# Call plot_pop for country code 'ARB'
plot_pop(fn, 'ARB')

