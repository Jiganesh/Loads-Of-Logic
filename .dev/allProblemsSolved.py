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

def difficulty (line):
    if "easy" in line.lower():
        return '<img src="https://img.shields.io/badge/-Easy-brightgreen">'
    elif "medium" in line.lower():
        return '<img src="https://img.shields.io/badge/-Medium-orange">'
    elif "hard" in line.lower():
        return '<img src="https://img.shields.io/badge/-Hard-red">'
    else :
        return line

for number in range(len(lines)):
    i= lines[number]
    p=i.index("```")
    writeReadme.write(str(number)+". ["+ i[:i.rindex("/")] +"]("+i[:p]+") "+  difficulty(i[p:])+"\n")

# #Additional Problems Here 
writeReadme.write(str(number)+'. [https://www.codingninjas.com/reverse-first-k-elements-of-queue](https://www.codingninjas.com/codestudio/guided-paths/data-structures-algorithms/content/118523/offering/1380947?leftPanelTab=0)'+difficulty('easy')+'\n') 

writeReadme.write( "### Yeah ofc we'd start counting from 0 duh !!")

f.close()
writeReadme.close()