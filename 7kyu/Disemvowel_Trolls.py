# Description:
# Trolls are attacking your comment section!
# A common way to deal with this situation is to remove all of the vowels from the trolls' comments, neutralizing the threat.
# Your task is to write a function that takes a string and return a new string with all vowels removed.
# For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".
# Note: for this kata y isn't considered a vowel.



def disemvowel1(st):
    b = [i for i in st]
    a = ["a","e","i","o","u","A","E","I","O","U"]
    for i in range(len(b)+1):
        for i in a:
            if i in b:
                b.remove(i)
    return ''.join(i for i in b)

def disemvowel2(st):
    a = ["a","e","i","o","u","A","E","I","O","U"]
    for i in a:
        st = st.replace(i,"")
    return st


st = 'This website is for losers LOL!'
print(disemvowel1(st))
print(disemvowel2(st))