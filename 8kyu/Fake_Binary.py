# Description:
# Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'. 
# Return the resulting string.

# Note: input will never be an empty string

#  1st Logic
def fake_bin(x):
    y=""
    for i in x:
        if int(i)<5:
            y= y+"0"
        else:
            y= y+"1"
    return y


#  2nd Logic
def fake_bin(x):
    return "".join("1" if i>='5' else "0" for i in x)