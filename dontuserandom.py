from random import randint, seed
count1 = 0
count2 = 0
count3 = 0
count4 = 0
count5 = 0
count6 = 0
count7 = 0
count8 = 0
count9 = 0
count10 = 0
count11 = 0
count12 = 0
count = [0] * 11

for i in range (1, 36):
    x = randint(1, 6)
    y = randint(1, 6)
    sum = x + y
    if sum == 1:
        count1+=1
        count[0]+=1
    elif sum == 2:
        count2+=1
    elif sum == 3:
        count3+=1
    elif sum == 4:
        count4+=1
    elif sum == 5:
        count5+=1
    elif sum == 6:
        count6+=1
    elif sum == 7:
        count7+=1
    elif sum == 8:
        count8+=1
    elif sum == 9:
        count9+=1
    elif sum == 10:
        count10+=1
    elif sum == 11:
        count11+=1
    else:
        count12+=1

"it rolled 1 this many times: "
print("it rolled 1 this many times: " + str(count1) + " The probability is: ", str((count1)/36))
print("it rolled 2 this many times: " + str(count2), str((count2)/36))
print("it rolled 3 this many times: " + str(count3), str((count3)/36))
print("it rolled 4 this many times: ",str((count4)/36))
print("it rolled 5 this many times: ",str((count5)/36))
print("it rolled 6 this many times: ",str((count6)/36))
print("it rolled 7 this many times: ",str((count7)/36))
print("it rolled 8 this many times: ",str((count8)/36))
print("it rolled 9 this many times: ",str((count9)/36))
print("it rolled 10 this many times: ",str((count10)/36))
print("it rolled 11 this many times: ",str((count11)/36))
print("it rolled 12 this many times: ", str((count12)/36))



