# Description:
# We need a function that can transform a number (integer) into a string.

# What ways of achieving this do you know?

# Examples (input --> output):
# 123  --> "123"
# 999  --> "999"
# -100 --> "-100"



#My code without Using str() function
def num_to_list(num):
    n=abs(num)
    a=[]

    while n>0:
        a.insert(0,int(n%10))
        n=(n-(n%10))/10
    if num<0:
        a.insert(0,'-')
    return a

def number_to_string(num):
    a=num_to_list(num)
    num_to_string_dict = {'-':'-',
                          0:'0',
                          1:'1',
                          2:'2',
                          3:'3',
                          4:'4',
                          5:'5',
                          6:'6',
                          7:'7',
                          8:'8',
                          9:'9',}
    return "".join(num_to_string_dict[i] for i in a)