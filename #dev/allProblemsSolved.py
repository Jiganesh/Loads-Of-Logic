f = open("README.md","r")
lines = f.readlines()
lines = sorted([x[x.index("- ")+2:] for x in lines if "- https" in x])

title = "## Problem Solved\n"


writeReadme = open("#dev/allProblemsSolved.md", "w")
writeReadme.write(title)
writeReadme.write("<ol>\n")
for i in lines:
    p=i.index("(")
    writeReadme.write("<li><a href ='"+ i + "'>"+i[:p]+"</a>"+i[p:]+"</li>\n")
'Additional Problems Here'
writeReadme.write(
    '<li><a href = "https://www.codingninjas.com/codestudio/guided-paths/data-structures-algorithms/content/118523/offering/1380947?leftPanelTab=0">https://www.codingninjas.com/reverse-first-k-elements-of-queue</a>(Easy)<li> '
    )
writeReadme.write("\n </ol>")



    
count = len(lines)

f.close()
writeReadme.close()