l1 = ["Batman", "Hulk", "Constantine", "Thor"]

#i = 1
#for item in l1:
#    if i%2!= 0:
#        print(f"Character that is in DC is {item}")
#    i += 1

# enumerate function
for index, item in enumerate(l1):
    if index%2==0:
        print(f"Character that is in DC is {item}")
