readingFile = open('index.html', 'r')
writingFile = open('.dev/sections.html','w')

allLines = "".join([i for i in readingFile])
allLines=allLines.replace('<ul>',"<ol>")
allLines=allLines.replace('</ul>',"</ol>")
slots = []

while "<details>" in allLines:
    i=allLines.find("<details>")
    j=allLines.find("</details>")
    print(allLines[i:j+10])
    slots.append(allLines[i:j+10])
    allLines = allLines [j+10:]
    break;
    

for i in slots:
    pass
    # writingFile.write(i+"\n\n")

readingFile.close()
writingFile.close()