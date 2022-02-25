inputSectionFile = open('.dev/sortingSectionsInput.txt', 'r')
outputSectionFile = open('.dev/sortingSectionsOutput.txt', 'w')


a = sorted([i for i in inputSectionFile.read().split('\n')])
for i in a :
    outputSectionFile.write(i + '\n')
    