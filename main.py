#1234567
print(" # # # Term 1 # # # ")
AES1 = int(input("AES: ")) # Ask for AES TERM 1
MAT1 = int(input("Maths 1: ")) # Ask for Maths 1
PHY1 = int(input("Physics 1: ")) # Ask for Physics 1
CP1 = int(input("Computer Programming 1: ")) # Ask for Computer programming 1
if AES1 >= 0 and AES1 <= 100: # Check if everything is valid
    if MAT1 >= 0 and MAT1 <= 100:
        if PHY1 >= 0 and PHY1 <= 100:
            if CP1 >= 0 and CP1 <= 100:
                print("Thank you, Term 1 is inputted.")
            else:
                print("That is not a valid input. Goodbye.")
                quit()
        else:
            print("That is not a valid input. Goodbye.")
            quit()
    else:
        print("That is not a valid input. Goodbye.")
        quit()
else:
    print("That is not a valid input. Goodbye.")
    quit()

print(" # # # Term 2 # # # ")
AES2 = int(input("AES: ")) # Ask for AES TERM 2
MAT2 = int(input("Maths 2: ")) # Ask for Maths 2
PHY2 = int(input("Physics 2: ")) # Ask for Physics 2
CP2 = int(input("Computer Programming 2: ")) # Ask for Computer programming 2
if AES2 >= 0 and AES2 <= 100: # Check if everything is valid
    if MAT2 >= 0 and MAT2 <= 100:
        if PHY2 >= 0 and PHY2 <= 100:
            if CP2 >= 0 and CP2 <= 100:
                print("Thank you, Term 2 is inputted.")
            else:
                print("That is not a valid input. Goodbye.")
                quit()
        else:
            print("That is not a valid input. Goodbye.")
            quit()
    else:
        print("That is not a valid input. Goodbye.")
        quit()
else:
    print("That is not a valid input. Goodbye.")
    quit()

print(" # # # Term 3 # # # ")
AES3 = int(input("AES: ")) # Ask for AES TERM 3
MAT3 = int(input("Maths 3: ")) # Ask for Maths 3
PHY3 = int(input("Physics 3: ")) # Ask for Physics 3
CP3 = int(input("Creative Design: ")) # Ask for Creative Design
if AES3 >= 0 and AES3 <= 100: # Check if everything is valid
    if MAT3 >= 0 and MAT3 <= 100:
        if PHY3 >= 0 and PHY3 <= 100:
            if CP3 >= 0 and CP3 <= 100:
                print("Thank you, Term 3 is inputted.")
            else:
                print("That is not a valid input. Goodbye.")
                quit()
        else:
            print("That is not a valid input. Goodbye.")
            quit()
    else:
        print("That is not a valid input. Goodbye.")
        quit()
else:
    print("That is not a valid input. Goodbye.")
    quit()
t1 = (AES1 + MAT1 + PHY1 + CP1)/4 # Term 1 avg marks
t2 = (AES2 + MAT2 + PHY2 + CP2)/4 # Term 2 avg marks
t3 = (AES3 + MAT3 + PHY3 + CP3)/4 # Term 3 avg marks
avg1 = (t1 + t2 + t3)/3 # avg marks overall
avg2 = (MAT2 + MAT3)/2 # avg marks of Maths 2 and Maths 3
if AES1 >= 40 and MAT1 >= 40 and PHY1 >= 40 and CP1 >= 40: # Check everything in term 1 are more than 40
    if AES2 >= 40 and MAT2 >= 40 and PHY2 >= 40 and CP2 >= 40: # Check everything in term 2 are more than 40
        if AES3 >= 40 and MAT3 >= 40 and PHY3 >= 40 and CP3 >= 40: # Check everything in term 3 are more than 40
            if avg1 >= 60: # Check avg overall is more than 60 or not
                if avg2 >= 65: # Check avg marks of Maths 2 and Maths 3 is more than 65 or not
                    if AES3 >= 60: # Check AES TERM 3 is more than 60
                        print("WELL DONE :) YOU PROGRESS!!") # Hooray!
                    else:
                        print("Sorry, you do not progress because you must have at least 60% in AES TERM 3.")
                else:
                    print("Sorry, you do not progress because you must have at least an average of 65% in Maths 2 and Maths 3.")
            else:
                print("Sorry, you do not progress because you must have at least ana average of 60% overall.")
        else:
            print("Sorry, you do not progress because you must get at least 40% in all subjects.")
    else:
        print("Sorry, you do not progress because you must get at least 40% in all subjects.")
else:
    print("Sorry, you do not progress because you must get at least 40% in all subjects.")
if avg1 == 100: # Are you smart?
    print("Wow you are so smart! 100 in everything! :)")
    quit()
else:
    quit()