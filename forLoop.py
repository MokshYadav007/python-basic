#list1 = ["Harry", 2],["Larry", 5],["Carry", 23],["Terry", 67]

#for item, Lollypop in list1:
   # print(item, Lollypop)

ITEMS = [int, float, "Rick", "Daryl", 1, 43, 4, 5, 6, 89, 2, 3, 65, 76, 89]
for item in ITEMS:
    if str(item).isnumeric() and item>=6:
        print(item)
