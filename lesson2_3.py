# 2.3 (1) write command line arguments and input file for at least three other lessons

import sys
seq = sys.argv[1]

input_seq = input('Enter a sequence/codon:').upper()

#letting the client decide which codon/sequence needs to be lower case and backwards

lower_case = input_seq.lower()

backwards = lower_case[::-1]

print(backwards)
