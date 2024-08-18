#!/usr/bin/env python3

# 6.5 Write code using find() and string slicing (see section 6.10) to extract the number at the end of the line below.
# Convert the extracted value to a floating point number and print it out.

text = "X-DSPAM-Confidence:    0.8475"
# find the position where the number lives
pos = text.find(':') + 1
# extract the number out of the string, remove spaces, convert to float
num = float(text[pos:].lstrip())

print(num)