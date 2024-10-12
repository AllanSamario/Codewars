# Description:
# Complete the method that takes a boolean value and return a "Yes" string for true, or a "No" string for false.


def bool_to_word(boolean):
    return "No" if not boolean else "Yes"

boo1=True
boo2=False
print(bool_to_word(boo1))
print(bool_to_word(boo2))