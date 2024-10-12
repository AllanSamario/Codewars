# Description:
# Make a simple function called greet that returns the most-famous "hello world!".

# Style Points
# Sure, this is about as easy as it gets. 
# But how clever can you be to create the most creative "hello world" you can think of? 
# What is a "hello world" solution you would want to show your friends?

import string
def greet():
    my_list = list(string.punctuation + string.digits + string.ascii_letters + " ")
    a = list("hello world!")
    s=""
    for i in a:
        if i in my_list:
            s+=i
    return s