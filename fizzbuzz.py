#!/usr/bin/python

for i in range(1, 100):
	output = ""
	if not i % 3:
		output += "Fizz"
	if not i % 5:
		output += "Buzz"
	if not output:
		output = str(i)
	print(output)
