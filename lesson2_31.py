# 2.3 (2) program to import the file
import sys

filename = sys.argv[1]
command = sys.argv[2]

with open(filename, "r") as f:
    lines = f.readlines()
    input_seq = "".join(lines).strip().lower()

# find start codon position and frame
#dna_sequence = "gcatcacgttatgtcgactctgtgtggcgtctgctggg"

position = input_seq.find("atg")
frame = (position%3)+1

if command == "position":
    print ('The position of the start codon/methionine is: ',position)
elif command == "frame":
    print ('The frame that has the start codon is:',frame)
else:
    print('none,bummer') No newline at end of file
