d1 = {}
#print(type(d1))
d2 = {"Batman":"Joker", "Superman":"ZOD", "Flash":"Reverse Flash","Lucifer":"GOD" }
#print(d2["Batman"])
#for adding extra
d2["Nightwing"] = "Deathshot"
d2["Constantine"] = "Anyone"
#for deleting

del d2["Nightwing"]
#print(d2.get("Batman"))
#d2.update({"SpiderMan":"Goblin"})
#print(d2.keys())
print(d2.items())
