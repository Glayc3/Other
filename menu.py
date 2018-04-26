print("Menu\n1. music\n2. history\n3. design and tech\n4. exit")
subjects = ["music", "history", "design and tech"]
while True:
    x = input("")
    if x in ["1","2","3"]:
        print ("you chose ", subjects[int(x)-1])
    elif x == "4":
        quit()
    else:
        print("error, try again")
