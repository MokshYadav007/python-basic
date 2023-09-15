import math
me = "Moksh"
a1 = 3
# a = "this is %s %s"%(me, a1)  # METHOD 1
#METHOD 2
#a = "this is {1} {0}"  # you can also leave these brackets blank
#b = a.format(me, a1)

# METHOD 3 WITH FSTRING
a = f"this is {me} {a1} {6} {4*32} {math.cos(55)}"
print(a)
