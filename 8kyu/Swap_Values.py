# I would like to be able to pass an array with two elements to my swapValues function to swap the values. However it appears that the values aren't changing.

# Can you figure out what's wrong here?


def swap_values(args): 
    a=args[0]
    args.remove(args[0])
    args.append(a)