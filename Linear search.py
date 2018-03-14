def linearSearch(myItem,myList):
    found = False
    position = 0
    while position < len(myList) and not found:
        if myList[position] == myItem:
            found = True
        position += 1
    return found

shopping = ["apples","banana","chocolate","pasta"]
item = input("what do you want to find?")
isitFound = linearSearch(item,shopping)
if isitFound:
    print("found lol")
else:
    print("no found xd")
