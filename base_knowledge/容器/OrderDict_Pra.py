from collections import OrderedDict




print('Regular dictionary:')
d = {}
d['a'] = 'A'
d['b'] = 'B'
d['c'] = 'C'
for k, v in d.items():
	print(k, v)

print('OrderedDict:')

d = OrderedDict()

d['a'] = 'A'
d['b'] = 'B'
d['c'] = 'C'
d['a']='E'


d.move_to_end('a')
for k, v in d.items():
	print(k, v)


print( 'a' in d)
print(len(d))

