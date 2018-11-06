# ----------------------------------------------
# This program gives the reverse complement of a
# DNA string.
# ----------------------------------------------
        
def ReverseComplement(s):
    s_dict = {'A':'T','T':'A','G':'C','C':'G'}
    return "".join([s_dict[base] for base in reversed(s)])
    
while True:
    s = str(input('Please type in the DNA string: '))

    count_length = len(s)

    print('The length of the DNA sequence is: ', count_length)
    print('The complementary DNA is: ', ReverseComplement(s))
    
    response = input("Would you like to perform another analysis? (YES/NO) ")

    if response != "YES":
        print("Ok. See you later.")
        break
