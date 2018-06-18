#Data Type
#there are mainly 5 type of datatype
#1)Numeric
  #int
a=5
print(a)
print(type(a))

  #long
b=622565458245434
print(b)
print(type(b))

  # float
c=6.5
print(c)
print(type(c))

  # complex
d=6+2j
print(d+3)
print(type(d))

#2) String
str="sunidhi dhiman" #here "sunidhi dhiman" is a string
print (type(str))
print (str.upper()) # return string in uppercase letters.
print(str.lower())  # return string in lowercase letters.
print (str.strip()) # returns a string with whitespace removed from the start and end.
print(str.split()) # returns a list of substrings separated by the given delimiter.
print (str)
print (str[1])
print (str[2:5]) #slicing
print (str[3:])
print (str*2) #repetition
print (str+'-name') #concatenation

#3) List (mutable)
li=['abcd',564,5.6,'nidhi',8.56]
print (type(li))
nli = [538,'pqr']
print (li)
print (li[2])
print (li[-2])
print (li[2:4])
print (li[1:])
#print (li[0][2])
print (nli*2)
print (li+nli)
#print (li.sort())
#print (li.reverse())

#4) Tuple (immutable)
tup=('abcd',564,5.6,'nidhi',8.56)
print (type(tup))
ntup = (538,'pqr')
print (tup)
print (tup[0])
print (tup[1:4])
print (tup[2:])
print (ntup*3)
print (ntup+tup)
print (len(tup))

#5) Dictionary
dict={}
ndict={"name":"sunidhi","rollno":"053","dept":"CSE"}
print(type(dict))
dict['one']="this is first"
dict[2]="ths is second"
print (dict['one'])
print (dict[2])
print (len(dict))
print (ndict)
print (ndict.keys())
print (ndict.values())
print (ndict.items())
print (ndict.clear())