x=[]
while True:
    try:
        x1 = int(input("how long the list (2<=ans>=30)?"))
        if x1<2 or x1>30:
            print("invalid number")
        else:
            break
    except TypeError:
        print("not a number")

for i in range(x1):
    x.append(int(input("enter number no "+ str(i+1))))
def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp=alist[i]
                alist[i] = alist[i+1]
                alist[i+1]=temp
bubbleSort(x)
print(x)
