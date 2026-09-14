# 2.3 (3)

import sys

# file and command used
#/Users/getthatbread101/Documents/GitHub/lessons/lesson2_32.py
#"/Users/getthatbread101/Library/Mobile Documents/com~apple~TextEdit/Documents/gc2.txt"

filename = sys.argv[1]

with open(filename, "r") as f:
    seq = f.read().strip().upper()

# whats the %G/C count?

count = 0
unt = 0
for nuc in seq:
    if nuc == 'G':
        count = count + 1
    if nuc == 'C':
        unt = unt + 1

m = (count + unt)/len(seq)*100

print (seq)
print ('G count : ',count)
print ('C count : ',unt)
print('G/C percent in the gene is:', m) No newline at end of file
