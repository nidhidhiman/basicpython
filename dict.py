# Create a dictionary to store name and marks of 10 students by user input.
print('enter credentials for 10 students')
dic = {}
for i in range(0,9):
         key = input('enter name of the std:')
         value = input('enter the marks of the std:')
         dic[key] = value
         print(dic)

#sorted according to the marks
print(sorted(dic.values()))
import operator
sort = sorted(dic.items(), key=operator.itemgetter(1))
print(sort)

#occurence of each letter in mississippi
h = ('mississippi')
print(h)
i = h.count('i')
m = h.count('m')
s = h.count('s')
p = h.count('p')
count_dict = {'M': m, 'I': i, 'S': s, 'P':p}
print(count_dict)