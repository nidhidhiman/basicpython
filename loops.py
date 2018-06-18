#A LOOP statement allows us to execute a statement or group of statements multiple times.
#there are basically 3 types of loops:
#1) WHILE loop: repeat the condition till true
a=0
while(a<10):
    print ("counting",a)
    a=a+1

b=10
while(a>0):
    print("reverse counting",a)
    a=a-1
#2) FOR loop: Executes a sequence of statements multiple times
num = 2
for a in range(1,9):
    print (num*a)

for i in range(1,6):
    for j in range (1,i+1):
        print (i,)
    print

for i in range (1,6):
    for j in range (5,i-1,-1):
        print ("*",)
    print

#3) NESTED loop: One or more loop inside any another while,for and do_while
i=2
while(i<50):
    j=2
    while(j<=(i/j)):
        if not(i%j):
            break
        j=j+1
    if(j>i/j):
        print(i,"is a prime")
    i=i+1

# LOOPS CONTROL STATEMENTS:Change execution from its normal sequence.
# BREAK: Terminates the loop statement.
for letter in 'sunidhi':
    if(letter=='d'):
        break
    print('current letter',letter)

for i in (1,3,4,6,8,2,9,5):
    if (i==8):
        print ("element found")
        break
    print(i,)

#CONTINUE:skip the remainder of its body and immediately retest its condition prior to reiterating.
for letter in 'sunidhi':
    if(letter=='d'):
        continue
    print('current letter',letter)

for i in (1,3,4,6,8,2,9,5):
    if (i==8):
        print ("element found")
        continue
    print(i,)

#PASS: pass keyword is used to execute nothing.
for letter in 'sunidhi':
    if(letter == 'd'):
        print("block letter")
        pass
    print('current letter',letter)