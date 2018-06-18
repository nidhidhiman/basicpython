#Decision Control System
#decides the direction of flow of program execution.
#there are basically 4 dcs:
#1) If statement
a=int(input("insert your favt no.-"))
if(a%2==0):
    print("your no is even")
#2) Else statement
b=int(input("insert your favt no.-"))
if(b%2==0):
    print("your no is even")
else:
    print("your no is odd")
#3) Elif statement
c=str(input("print your name"))
if(c=="sunidhi"):
    print("you are from cse dept")
elif(c=="neha"):
    print("you are from ece dept")
else:
    print("none of above")

#4) Nested decision statement
d=int(input("insert any number"))
if(d%2==0):
    if(d==2):
        print("your no is 2")
    else:
        print("your no is div. by 2")
elif(d%3==0):
    if(d==3):
        print("your no is 3")
    else:
        print("your no is div. by 3")
else:
    print("incorrect no.")
