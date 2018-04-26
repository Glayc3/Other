while True:
    w = input("input width")
    l = input("input length")
    try:
        w2 = int(w)
        l2 = int(l)
        break
    except:
        print("you didn't input valid digits, try again")

area = w2 * l2
if w2 == l2:
    print("this is a square of area", area)
else:
    print("this is a rectangle of area", area)
