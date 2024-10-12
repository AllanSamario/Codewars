# Description:
# Write a function that when given a URL as a string,
# parses out just the domain name and returns it as a string. For example:

# * url = "http://github.com/carbonfive/raygun" -> domain name = "github"
# * url = "http://www.zombie-bites.com"         -> domain name = "zombie-bites"
# * url = "https://www.cnet.com"                -> domain name = cnet"


import re

def domain_name(url):
    str = ['www.']
    str2 = re.findall(".+//", url)

    if (re.findall("www.", url) == str):
        x = re.findall(".*www.", url)
        a_1 = url.removeprefix(x[0])

        y = re.findall("\..*", a_1)
        a_2 = a_1.removesuffix(y[0])

    elif str2 == []:
        y = re.findall("\..*", url)
        a_2 = url.removesuffix(y[0])
    
    else:
        a_1 = url.removeprefix(str2[0])
        y = re.findall("\..*", a_1)
        a_2 = a_1.removesuffix(y[0])

    return a_2