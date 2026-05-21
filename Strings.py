len("Hello World")
s='Hello World'
print(s)
print('s[0]:',s[0])
print('s[1]:',s[1])
print('s[2]:',s[1])
print('s[1:]',s[1:])
print(s[:3])
print(s[:])
#we can also use negative indexing to go backword
#last letter(one index behind 0 so it loops back around)
print(s[-1])
print('s[::1]',s[::2])
print('s[::1]',s[::2])
print('s[::-1]',s[::-1])
# ## String Properties
print(s)
#cccccconcatinate Strings
s  + 'concatenate me!'
s= s+'concatenate me!'
print(s)
letter = 'z'
letter*10
print('letter:',letter)
print('s.upper()',s.upper())
print('s.lower()',s.lower())
print('s.split()',s.split())
print("s.split('w')",s.split('w'))
print(' This is a string with an {p}'.format(p='insert'))
print('One: {p},Two: {p}'.format(p='Hi'))
print('object 1: {a},object 2:{b},object 3:{c}'.format(a=1,b='two',c=12.3))


