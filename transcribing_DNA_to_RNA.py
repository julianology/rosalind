# ----------------------------------------------
# This program counts transcribes a DNA sequence
# to its RNA counterpart. Take note that T or
# Thymine will be replaced with U or Uracil.
# ----------------------------------------------

while True:
    s = str(input('Please type in the DNA string: '))

    count_length = len(s)
    transcribed_DNA = s.replace('T', 'U')
    
    print('The length of the DNA sequence is: ', count_length)
    print('The transcribed RNA is: ', transcribed_DNA)
    
    response = input("Would you like to perform another analysis? (YES/NO) ")

    if response != "YES":
        print("Ok. See you later.")
        break
