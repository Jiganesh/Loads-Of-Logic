f = open("README.md","r")
lines = f.readlines()
lines = sorted([x[x.index("- ")+2:] for x in lines if "- https" in x])

title = "## Problem Solved\n"
writeReadme = open(".dev/allProblemsSolved.md", "w")
writeReadme.write(title)
count = len(lines)
print(count+1)
#writeReadme.write('<p style ="display: inline">Problems Solved </p>')
#writeReadme.write('<p id="count" style="display: inline">' + str(count) + '</p>\n')

writeReadme.write("<ol>\n")
for i in lines:
    p=i.index("(")
    writeReadme.write("<li><a href ='"+ i[:i.rindex("/")] + "'>"+i[:p]+"</a>"+i[p:]+"</li>\n")
'Additional Problems Here'
writeReadme.write(
    '<li><a href = "https://www.codingninjas.com/codestudio/guided-paths/data-structures-algorithms/content/118523/offering/1380947?leftPanelTab=0">https://www.codingninjas.com/reverse-first-k-elements-of-queue</a>(Easy)</li> '
    )
writeReadme.write("\n </ol>")    


f.close()
writeReadme.close()