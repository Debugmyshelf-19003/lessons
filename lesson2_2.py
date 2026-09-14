# 2.2 Write a command-line program for manipulating a DNA sequence

#filename = "/Users/getthatbread101/Downloads/sequence.txt"
import sys
# sys.argv[0] -> lesson2_2.py python file
#getting filename and command from command line
filename = sys.argv[1] # DNA file like this /Users/getthatbread101/Downloads/sequence.txt
command = sys.argv[2] # command/argument like Compliment, reverse or reverse compliment

#open and read dna sequence from the file
with open(filename, "r") as f:
    lines = f.readlines()
    input_seq = "".join(lines).strip()

def reverse(seq):
    seq =seq.upper()
    seq = seq[::-1]
    return seq

def compliment(seq):
    seq = seq.upper()
    newseq = ""

    nucleotides = 'ACGT'
    compliments = 'TGCA'

    for nuc in seq:
        i = nucleotides.find(nuc)

        if i >= 0:
            comp = compliments[i]
        else:
            comp = nuc
        newseq = newseq + comp
    return newseq

def reverseCompliment(seq):
    seq = seq.upper()
    newseq = ""
    for nuc in seq:
        newseq = compliment(nuc) + newseq
    return newseq

# Print original DNA sequence
print("DNA sequence:", input_seq)

# Perform the command it was given
if command == "compliment":
    print("The Compliment sequence: ", compliment(input_seq))
elif command == "reverse":
    print("The Reverse sequence:",reverse(input_seq))
elif command == "reverseCompliment":
    print("The Reverse compliment:", reverseCompliment(input_seq))
else:
    print("Invalid Command")
