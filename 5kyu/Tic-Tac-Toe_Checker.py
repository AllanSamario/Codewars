# Description:
# If we were to set up a Tic-Tac-Toe game, we would want to know whether the board's current state is solved,
# wouldn't we? Our goal is to create a function that will check that for us!

# Assume that the board comes in the form of a 3x3 array, where the value is 0 if a spot is empty,
# 1 if it is an "X", or 2 if it is an "O", like so:

# [[0, 0, 1],
#  [0, 1, 2],
#  [2, 1, 0]]
# We want our function to return:
# -1 if the board is not yet finished AND no one has won yet (there are empty spots),
# 1 if "X" won,
# 2 if "O" won,
# 0 if it's a cat's game (i.e. a draw).
# You may assume that the board passed in is valid in the context of a game of Tic-Tac-Toe.


def is_solved(ar):
    ret = 0
    for i in range(3):
        for j in range(3):
            if ar[i][j] == 0:
                if ( (ar[0][0]==1 and ar[0][1]==1 and ar[0][2]==1) 
                    or (ar[1][0]==1 and ar[1][1]==1 and ar[1][2]==1)
                    or (ar[2][0]==1 and ar[2][1]==1 and ar[2][2]==1)
                    
                    or (ar[0][0]==1 and ar[1][0]==1 and ar[2][0]==1)
                    or (ar[0][1]==1 and ar[1][1]==1 and ar[2][1]==1)
                    or (ar[0][2]==1 and ar[1][2]==1 and ar[2][2]==1)
                    
                    or (ar[0][0]==1 and ar[1][1]==1 and ar[2][2]==1)
                    or (ar[0][2]==1 and ar[1][1]==1 and ar[2][0]==1)):
                    ret = 1
                    break
                elif ( (ar[0][0]==2 and ar[0][1]==2 and ar[0][2]==2) 
                    or (ar[1][0]==2 and ar[1][1]==2 and ar[1][2]==2)
                    or (ar[2][0]==2 and ar[2][1]==2 and ar[2][2]==2)
                    
                    or (ar[0][0]==2 and ar[1][0]==2 and ar[2][0]==2)
                    or (ar[0][1]==2 and ar[1][1]==2 and ar[2][1]==2)
                    or (ar[0][2]==2 and ar[1][2]==2 and ar[2][2]==2)
                    
                    or (ar[0][0]==2 and ar[1][1]==2 and ar[2][2]==2)
                    or (ar[0][2]==2 and ar[1][1]==2 and ar[2][0]==2)):
                    ret = 2
                    break
                else:
                    ret = -1
            elif ar[i][j] != 0:
                if ( (ar[0][0]==1 and ar[0][1]==1 and ar[0][2]==1) 
                    or (ar[1][0]==1 and ar[1][1]==1 and ar[1][2]==1)
                    or (ar[2][0]==1 and ar[2][1]==1 and ar[2][2]==1)
                    
                    or (ar[0][0]==1 and ar[1][0]==1 and ar[2][0]==1)
                    or (ar[0][1]==1 and ar[1][1]==1 and ar[2][1]==1)
                    or (ar[0][2]==1 and ar[1][2]==1 and ar[2][2]==1)
                    
                    or (ar[0][0]==1 and ar[1][1]==1 and ar[2][2]==1)
                    or (ar[0][2]==1 and ar[1][1]==1 and ar[2][0]==1)):
                    ret = 1
                    break
                elif ( (ar[0][0]==2 and ar[0][1]==2 and ar[0][2]==2) 
                    or (ar[1][0]==2 and ar[1][1]==2 and ar[1][2]==2)
                    or (ar[2][0]==2 and ar[2][1]==2 and ar[2][2]==2)
                    
                    or (ar[0][0]==2 and ar[1][0]==2 and ar[2][0]==2)
                    or (ar[0][1]==2 and ar[1][1]==2 and ar[2][1]==2)
                    or (ar[0][2]==2 and ar[1][2]==2 and ar[2][2]==2)
                    
                    or (ar[0][0]==2 and ar[1][1]==2 and ar[2][2]==2)
                    or (ar[0][2]==2 and ar[1][1]==2 and ar[2][0]==2)):
                    ret = 2
                    break
    return ret