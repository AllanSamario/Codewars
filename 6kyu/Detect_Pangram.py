# Description:
# A pangram is a sentence that contains every single letter of the alphabet at least once. 
# For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, 
# because it uses the letters A-Z at least once (case is irrelevant).

# Aim:
# Given a string, detect whether or not it is a pangram. 
# Return True if it is, False if not. Ignore numbers and punctuation.

import string
def is_pangram(st):
    s1 = set(string.ascii_lowercase)
    return s1.intersection(set(st.lower())) == s1