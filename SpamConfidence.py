#!/usr/bin/env python3

# 7.2 Write a program that prompts for a file name, then opens that file and reads through the file, 
# looking for lines of the form:
#   X-DSPAM-Confidence:    0.8475
# Count these lines and extract the floating point values from each of the lines and compute the average 
# of those values and produce an output as shown below. 
# Do not use the sum() function or a variable named sum in your solution.
# You can download the sample data at http://www.py4e.com/code3/mbox-short.txt 
# When you are testing below enter mbox-short.txt as the file name.

# Desired Output:
# Average spam confidence: 0.7507185185185187

# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
num = 0.0
for line in fh:
	line = line.rstrip()
	if not line.startswith("X-DSPAM-Confidence:"):
		continue
	pos = line.find(':') + 1
	num += float(line[pos:].lstrip())
	count += 1
print('Average spam confidence:', num / count)

# Enter file name: mbox-short.txt
# Average spam confidence: 0.7507185185185187