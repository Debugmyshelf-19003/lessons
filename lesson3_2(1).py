import sys

filename = sys.argv[1]
with open(filename) as f:
    DNA = f.read().upper()

bases = {"A":"T", "T":"A", "G":"C", "C":"G"} #making a dictionary with key

complement = "" #using set to add the new value from the loop

for base in DNA:
    complement = complement + bases[base] #using key from the dictionary to run a loop

reverse_complement = complement[::-1]

print("original DNA sequence:", DNA)
print("complement:", complement)
print("reverse_complement:", reverse_complement)
