f = open("README.md","r")
lines =f.readlines()
lines = sorted([x[x.index("- ")+2:] for x in lines if "- https" in x])

title = "## Problems Solved\n"
writeReadme = open(".dev/allProblemsSolved.md", "w")
writeReadme.write(title)

array =[0,0,0]
def difficulty (line):
    if "easy" in line.lower():
        array[0]+=1
        return '<img src="https://img.shields.io/badge/-Easy-brightgreen">'
    elif "medium" in line.lower():
        array[1]+=1
        return '<img src="https://img.shields.io/badge/-Medium-blue">'
    elif "hard" in line.lower():
        array[2]+=1
        return '<img src="https://img.shields.io/badge/-Hard-red">'
    else :
        return line
    

for number in range(len(lines)):
    i= lines[number]
    p=i.index("```")
    writeReadme.write(str(number)+". ["+ i[:i.rindex("/")] +"]("+i[:p]+") "+  difficulty(i[p:])+"\n")


# #Additional Problems Here 
writeReadme.write(str(number)+'. [https://www.codingninjas.com/reverse-first-k-elements-of-queue](https://www.codingninjas.com/codestudio/guided-paths/data-structures-algorithms/content/118523/offering/1380947?leftPanelTab=0) '+difficulty('easy')+'\n') 



easy = "<img src='https://img.shields.io/badge/"+str(array[0])+" -Easy Problems Solved-brightgreen '> " 
medium = "<img src='https://img.shields.io/badge/"+str(array[1])+" -Medium Problems Solved-blue '> "
hard = "<img src='https://img.shields.io/badge/"+str(array[2])+" -Hard Problems Solved-red '> "



writeReadme.write( "\n### Yeah ofc we'd start counting from 0 duh !!\n")
writeReadme.write(easy)
writeReadme.write(medium)
writeReadme.write(hard)

f.close()
print(array, sum(array))
f.close()
writeReadme.close()