f1 = open("jesse.txt")

try:
    f = open("does.txt")

except Exception as e:
    print(e)

else:
    print("this will only run if except")
    
finally:
    print("run this anyway")
    #f.close()
    f1.close()

print("Important stuff")
