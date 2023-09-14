#i = 0

#while(True):
    #if i+1<5:
        #i = i + 1     #with this it will countinue from 5 , you can write any function you want
        #continue

    #print(i +1, end = " ")
    #if i == 44:
        #break    #stop the loop

    #i = i + 1

while(True):
    inp  = int(input("Enter Your Age\n" ))
    if inp>100:
        print("You Are DAMN OLD\n")
        break
    else:
        print("You are still YOUNG\n")
        continue
