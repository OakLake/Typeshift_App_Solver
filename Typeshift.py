import enchant
d = enchant.Dict("en_US")

import os
os.system("clear")



def makeWords(lettersSet):

    if len(lettersSet) == 1:
        return lettersSet[0]

    comb = []
    for c in lettersSet[0]:
        for d in lettersSet[1]:
            comb.append(c+d)

    lettersSet[0:2] = [comb]

    return makeWords(lettersSet)




nCols = int(input('Input the number of letters: '))
lettersSet = []
for i in range(0,nCols):
    # requestTxt = "Enter "
    temp = input("Enter letters " + str(i+1)+": ")
    letters = [c for c in temp]
    lettersSet.append(letters)



possibilities = makeWords(lettersSet)


valids = []
for p in possibilities:
    if d.check(p):
        valids.append(p)

print (" ")
print (" ")
print ("Words Found:")
print (" ")

k = 0
for v in valids:
    print (k,v)
    k += 1

print (" ")
print (" ")


##
