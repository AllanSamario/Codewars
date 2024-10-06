# Description:
# Given a string indicating a range of letters, return a string which includes all the letters in that range, including the last letter.
# Note that if the range is given in capital letters, return the string in capitals also!

# Examples
# "a-z" ➞ "abcdefghijklmnopqrstuvwxyz"
# "h-o" ➞ "hijklmno"
# "Q-Z" ➞ "QRSTUVWXYZ"
# "J-J" ➞ "J"


import string

def gimme_the_letters(sp):
    all = string.ascii_letters
    str=""
    for i in range(all.find(sp[0]),all.find(sp[2])+1):
        str=str + all[i]
    return str