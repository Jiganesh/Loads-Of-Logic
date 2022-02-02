f = open("README.md","r")
lines =[i for i in f.readlines()]
link = lines[2]
number =link[link.index("d-")+2:link.index("-brightgreen") ] 
print(number)
f.close()