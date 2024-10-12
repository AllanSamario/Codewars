# Description:
# ATM machines allow 4 or 6 digit PIN codes 
# and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits.
# If the function is passed a valid PIN string, return true, else return false.

# Examples (Input --> Output)
# "1234"   -->  true
# "12345"  -->  false
# "a234"   -->  false

#Code
import re

numValidator = r'[0-9]+'
def validate_pin(pin):
    y = re.findall(numValidator,pin)
    if y and len(y[0]) == len(pin) and (len(pin) == 4 or  len(pin) == 6):
        return True
    return False