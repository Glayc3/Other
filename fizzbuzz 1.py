#12/10/17

x= int(input("select number between 1-100"))
y= int(input("select number between 1-100"))

for i in range(100):

    if i%x == 0 and i%y == 0:
        print("fizzbuzz")

    elif i%x == 0:
        print("fizz")

    elif i%y == 0:
        print("buzz")

    else:
        print(i)
