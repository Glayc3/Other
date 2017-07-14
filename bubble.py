x=[]
while True:
	try:
        x1 = int(input("how long the list?"))
        if x1<2 or x1>30:
            print("invalid number")
        else:
            break
    except ValueError:
        print("not a number")
for i in range(x1):
    x.append(int(input("enter number no "+ i)))
def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp=alist[i]
                alist[i] = alist[i+1]
                alist[i+1]=temp
bubbleSort(x)
print(x)
