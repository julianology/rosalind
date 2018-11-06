# ----------------------------------------------
# This program counts the number of times that
# the nucloebases adenine (A), cytosine (C),
# guanine (G), and thymine (T) occured in a DNA
# strand length respectively. It will also give
# you the length of the DNA sequence.
# ----------------------------------------------

while True:
    s = str(input('Please type in the DNA string: '))

    count_length = len(s)
    count_A = s.count('A')
    count_C = s.count('C')
    count_G = s.count('G')
    count_T = s.count('T')
    
    print('The length of the DNA sequence is: ', count_length,
          '\nHere is the breakdown of the nucleotides in the DNA sequence... ',
          '\nA or Adenosine: ', count_A,
          '\nC or Cytosine:  ', count_C,
          '\nG or Guanine:   ', count_G,
          '\nT or Thymine:   ', count_T, 
    )

    response = input("Would you like to perform another analysis? (YES/NO) ")

    if response != "YES":
        print("Ok. See you later.")
        break
