from turtle import *

ht()
#-----------------------------------------------------------#

turn_angle = 90
forward_distance = 1
speed(0)

#-----------------------------------------------------------#

def getNextFractalString(iterations):
    string = ""
    xstring = ""

    for i in range(iterations):
        prenewstring = string[::-1]
        newstring = ""

        for i in prenewstring:
            newstring = newstring + ("L" if i == "R" else "R")

        xstring = "R" + newstring
        string = string + xstring


    return xstring


#-----------------------------------------------------------#
i = 0
while True:
    i += 1
    print("Doing level " + str(i) + " : Size " + str((2**i)/2+1) + " : Total Size " + str(2**i+1))

    for move in getNextFractalString(i):
        fd(forward_distance)


        if move == "R":
            right(turn_angle)
        else:
            left(turn_angle)


    print("Done")



#-----------------------------------------------------------#

while True:
    pass
