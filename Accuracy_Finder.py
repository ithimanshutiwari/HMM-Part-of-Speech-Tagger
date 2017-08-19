l1=[]
l2=[]
with open('output') as f1:
	for line in f1:
		for i in line.split():
			l1.append(i)
			


with open('tagged_brown_corpus') as f2:
	for line in f2:
		for i in line.split():
			l2.append(i)

l2=l2[0:len(l1)]
c1=0
c2=0
for a, b in zip(l1, l2):
    c1+=1	
    if a != b:
    	c2+=1.0
print (c1-c2),c1,(c1-c2)/c1
