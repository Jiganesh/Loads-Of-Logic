readingFile = open('index.html', 'r')
writingFile = open('.dev/sections.html','w')

allLines = "".join([i for i in readingFile])
allLines=allLines.replace('<ul>',"<ol>")
allLines=allLines.replace('</ul>',"</ol>")
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