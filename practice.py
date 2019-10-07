f = open("listofwords.txt", "r")
words=f.readlines()
wordlists=[]
for x in words:
    wordlists.append(x.strip().split(","))
f.close()
y=open("listofwords.txt","w")
c=str(wordlists)
y.write(c)