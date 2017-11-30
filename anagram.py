from time import sleep
for i in range(123456789):
    for r in range(8):
        x = (r+1)*i
        t = [int(y) for y in str(i)]
        x2 = [int(e) for e in str(x)]
        if t in x2:
            print(i)
            print("YES")
            break
        else:
            pass
    print(i)
    print("NO")
