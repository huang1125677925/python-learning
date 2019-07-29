import pyfpgrowth

transactions = [[1, 2, 5],
                [2, 4],
                [2, 3],
                [1, 2, 4],
                [1, 3],
                [2, 3],
                [1, 3],
                [1, 2, 3, 5],
                [1, 2, 3]]


patterns = pyfpgrowth.find_frequent_patterns(transactions, 2)


for key,value in patterns.items():
	print("{0}-------{1}".format(key,value))



rules = pyfpgrowth.generate_association_rules(patterns, 0.5)

for key,value in rules.items():
	print("{0}-------{1}".format(key,value))


print("{:X}".format(100))