from random import randint as random
print("you'll throw two digital dice and lets see what points you get\nif you get two that are the same number your points double wow")
input("ready to throw 2 dice???")
d1 = random(1,6)
d2 = random(1,6)
score1 = int(d1) + int(d2)
if d1 == d2:
    score2 = score1*2
    print("you got a double man!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
else:
    score2 = score1
print("your score is", score2)
