import random

_author_ = 'Melissa Hurley'

# Application to convert BPM to Frequency Hz, Musical Notation and Octave
# Enter the BPM to be calculated
# The number entered will be converted and displayed as Frequency Hz, Notation and Octave
# The Notation will then be integrated to activate notes on a digital keyboard display
# The output will be integrated through speakers
# A visual component will display the conversion of Frequency Hz to Light Wave Frequency
#
# (automation will be later integrated using a pulse rate monitor as a controller)
#
#
# Input
mNotation = input("Enter BPM: ")
# Convert
mBPM = float(mNotation)
mNote = str("A"), str("B"), str("C"), str("D"), str("E"), str("F"), str("G")
mHalf = str("#")
mWhole = str("Whole")
mFlat = str("Flat")
mOctave = int(1)
mNothing = str("None")
p = 440
# Compute
mFrequency = mBPM * 0.02
# Note Octave conversion
mScale = mOctave * round(mFrequency)
# Output
print("The Frequency Hz equivalent is: " + str(mFrequency))
print("The rounded frequency is: " + str(round(mFrequency)))
print("The ASCii Conversion of the rounded frequency is: " + chr(round(mFrequency)))

# lists the range of notes that can be played on a keyboard
list_note = mNote
for n in list_note:
    if mBPM < 20000:
        print("The note is: ", {n})
    else:
        print("The note is: " + str(mNothing))
while True:
    if mBPM >= 440:
        print("The note is " + mWhole)
        break
    elif mBPM >= 220:
        print("The note is " + mHalf)
        break
    else:
        print("The note is " + mFlat)
        break
# Output of the octave in which the note will be played(will implement restriction to 8)
print("The Octave is: " + str(mScale))
# Indexing a dictionary of the note list
a_dictionary = list_note
keys_list = list(a_dictionary)
# Random shuffle of the list being indexed
random.shuffle(keys_list)
# Chooses a string from the list
a_key = keys_list[0]
# Output
print("The note that will be played is: " + str(a_key))
