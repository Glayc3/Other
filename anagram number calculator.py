from time import sleep
no_of_yes = 0

for i in range(123456789):
    for r in range(8):
        x = (r+1)*i
        t = [int(y) for y in str(i)]
        x2 = [int(e) for e in str(x)]
        if t in x2:
            print(i)
            print("YES " + str((r+1)))
            no_of_yes += 1
            continue
        else:
            pass
    print(i)
    print("NO")
print(str(no_of_yes))
