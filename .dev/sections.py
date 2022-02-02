readingFile = open('README.md', 'r')
writingFile = open('.dev/sections.md','w')

allLines = "\n".join(sorted([i for i in readingFile]))
slots = []
while "<details>" in allLines:
    i=allLines.find("<details>")
    j=allLines.find("</details>")
    slots.append(allLines[i:j+10])
    allLines = allLines [j+10:]

for i in slots:
    writingFile.write(i+"\n\n")

readingFile.close()
writingFile.close()