f = open("README.md","r")
lines = f.readlines()
lines = sorted([x for x in lines if x.startswith("- https")])

    
writeReadme = open("#dev/allProblemsSolved.md", "w")
for i in lines:
    writeReadme.write(i)
    
count = len(lines)

f.close()
writeReadme.close()