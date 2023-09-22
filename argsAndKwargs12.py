#def function_name_print(a, b, c, d, e):
#    print(a, b, c, d, e)

def funargs(normal, *argsmoksh, **kwargs):
    print(normal)
    for item in argsmoksh:
        print(item)
    print("\nNow i would like to introduce some of their occupation")
    for key, value in kwargs.items():
        print(f"{key} is  {value}")
# function_name_print("Harry", "Bruce", "Vishal", "Skillf", "Daryl")

har = ["Harry", "Bruce", "Vishal", "Skillf", "Daryl"]
normal = "I am a normal argument"
kw = {"Harry":"Coder", "Bruce": "batman", "Daryl": "Hunter"}
funargs(normal, *har, **kw)
