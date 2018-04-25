# Samantha Ngo
# List Comprehensions

# First Task: Check if password has upper and lower case letters and at least
# 1 number

UC_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LC_LETTERS = "abcdefghijklmnopqrstuvwxyz"
digits = "0123456789"

def checkPass(password):
    uppers = [1 for x in password if x in UC_LETTERS]
    print "UPPERS: ", uppers
    lowers = [1 for x in password if x in LC_LETTERS]
    print "LOWERS: ", lowers
    numbers = [1 for x in password if x in digits]
    print "NUMS: ", numbers

    if ((len(uppers) != 0) and (len(lowers) != 0) and (len(numbers) != 0)):
        print "Pass: ", password, " meets criteria."
        return True;
    else:
        print "Pass: ", password, " DOES NOT meet criteria."
        return False

checkPass("HelloWorld")
checkPass("HelloWorld1!")
checkPass("H")

print  "================================================================"

# Second Task: Given a password, return the password's strength rating
# Password MUST have upper and lower case letters, include numbers, and
# Non-Alphanumeric nums: . ? ! & # , ; : - _ *

'''
Strength Strategies:
- Dictionary Attack -> Passphrases
- Character Attack -> Increase # of characters

Min: 8 letters(>0 Upper & >0 Lower) + 1 non-alphanumeric + 1 number
Medium: 12 letters + 2 non-alpha + 1 number
Strong: 15 letters + 4 non-alpha + 2 numbers 
'''

nonAlphas = ".?!&#,;:-_*"

def strength(password):
    uppers = len([1 for x in password if x in UC_LETTERS])
    print "UPPERS: ", uppers
    lowers = len([1 for x in password if x in LC_LETTERS])
    print "LOWERS: ", lowers
    numbers = len([1 for x in password if x in digits])
    print "NUMS: ", numbers
    nons = len([1 for x in password if x in nonAlphas])
    print "NONS: ", nons

    # Top-Down Criterion Check
    if (uppers + lowers >= 15 and 
        print "Pass: ", password, " meets criteria."
        return True;
    else:
        print "Pass: ", password, " DOES NOT meet criteria."
        return False

strength("HelloWorld")
strength("HelloWorld1!")
strength("H")
