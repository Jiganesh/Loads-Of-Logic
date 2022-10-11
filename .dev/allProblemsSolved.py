import matplotlib.pyplot as plt
import seaborn as sns

f = open("README.md","r")
lines =[ i for i in f.readlines()]


# Extracting previous problems solved count
link = lines[2]
prevProblemsSolved =int(link[link.index("d-")+2:link.index("-brightgreen")])

lines = sorted([x[x.index("- ")+2:] for x in lines if "- https" in x])




title = "## Problems Solved\n"
writeReadme = open(".dev/allProblemsSolved.md", "w")
writeReadme.write(title)


# Initialize Extra Problems Solved here which are not in form of links
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
    try:
        p=i.index("```")
    except:
        print(i)
    writeReadme.write(str(number)+". ["+ i[:i.rindex("/")] +"]("+i[:p]+") "+  difficulty(i[p:])+"\n")

# #Additional Problems Here 
writeReadme.write(str(number)+'. [https://www.codingninjas.com/reverse-first-k-elements-of-queue](https://www.codingninjas.com/codestudio/guided-paths/data-structures-algorithms/content/118523/offering/1380947?leftPanelTab=0) '+difficulty('easy')+'\n') 
writeReadme.write(str(number)+'. [https://www.codingninjas.com/minimum-subset-difference](https://www.codingninjas.com/codestudio/problems/partition-a-set-into-two-subsets-such-that-the-difference-of-subset-sums-is-minimum_842494?leftPanelTab=0) '+difficulty('medium')+'\n') 
writeReadme.write(str(number)+'. [https://www.codingninjas.com/longest-repeating-subsequence](https://www.codingninjas.com/codestudio/problems/longest-repeating-subsequence_1118110?leftPanelTab=1) '+difficulty('medium')+'\n') 
writeReadme.write(str(number)+'. [https://www.codingninjas.com/matrix-chain-multiplication](https://www.codingninjas.com/codestudio/problems/matrix-chain-multiplication_975344?leftPanelTab=0) '+difficulty('medium')+'\n') 
writeReadme.write(str(number)+'. [https://www.codingninjas.com/partitions-with-given-difference](https://www.codingninjas.com/codestudio/problems/partitions-with-given-difference_3751628?source=youtube&campaign=striver_dp_videos&utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_dp_videos) '+difficulty('medium')+'\n') 

# create data
names = ['Easy','Medium', 'Hard']
size = array
 
# Create a circle at the center of the plot
my_circle = plt.Circle( (0,0), 0.7, color='white')

# Custom wedges
plt.pie(size, labels=names, wedgeprops = { 'linewidth' : 7, 'edgecolor' : 'white' }, colors=["Green", "Blue", "Red"])
p = plt.gcf()
p.gca().add_artist(my_circle)
plt.savefig(".dev/donutDifficulty.png", bbox_inches='tight')
plt.close()


easy = "<img src='https://img.shields.io/badge/"+str(array[0])+" -Easy Problems Solved-brightgreen '> " 
medium = "<img src='https://img.shields.io/badge/"+str(array[1])+" -Medium Problems Solved-blue '> "
hard = "<img src='https://img.shields.io/badge/"+str(array[2])+" -Hard Problems Solved-red '> "

writeReadme.write( "\n### Yeah ofc we'd start counting from 0 duh !!\n")
writeReadme.write(easy)
writeReadme.write(medium)
writeReadme.write(hard)

print("Easy, Medium and Hard problems respectively are ", array)
print("Total problems solved are ",sum(array))

f.close()
writeReadme.close()

# CODE BELOW THIS UPDATES README.md

f = open("README.md","r")
lines = [i for i in f][3:]

writeNewReadme = open("README.md", "w")
writeNewReadme.write('<img src= ".dev/LoadsOfLogic.png" height= 40%  width = 140%>\n\n')
writeNewReadme.write('<a href ="https://github.com/Jiganesh/High-On-DSA/blob/main/.dev/allProblemsSolved.md"><img src="https://img.shields.io/badge/Total Problems Solved- ' + str(sum(array)) + ' -brightgreen?"></a> <img src="https://img.shields.io/badge/Licensed- MIT -blue?">')
writeNewReadme.write(' <img src="https://img.shields.io/badge/Problems Solved Today-' +str(sum(array)-prevProblemsSolved)+'-orange?">\n\n')

print("New Problem added since last Update are :",sum(array)-prevProblemsSolved)
for i in lines:
    writeNewReadme.write(i)

f.close()
writeNewReadme.close()

