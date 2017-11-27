from time import sleep as wait

def slowtext(text,sec):
    print(text)
    wait(sec)

slowtext("gonna split your price",0.5)
slowtext("use it on the jerks who try and pay less on meals",0.5)

while True:
    try:
        people = float(input("how many of you dudes?"))
        break
    except:
        slowtext("write properly",0.5)

while True:
    try:
        bill = float(input("how much the bill(just the number)"))
        break
    except:
        slowtext("write properly",0.5)
price_each = bill/people
answer = str(round(float(price_each), 2))
slowtext("each pay £" + answer,0.5)
