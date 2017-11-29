for i in range(123456789):
    for r in range(8):
        x = (r+1)*i
        t = [int(y) for y in str(i)]
        x2 = [int(e) for e in str(x)]
        if t in x:
            print(i)
            print("YES")
        else:
            pass


        
