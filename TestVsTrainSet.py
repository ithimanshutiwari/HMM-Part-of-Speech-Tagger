totalLines=57066;
factor=90
remain=100-factor

file1 = open('tagged_brown_corpus')
file2 = open('untagged_brown_corpus')


out1 = open('tagged_brown90','w')
out2 = open('tagged_brown10', 'w')
out3 = open('untagged_brown10','w')
 

cnt=0
firstSize=int(factor*totalLines/100.0)
secondSize=totalLines-firstSize
for line in file1: 
	if cnt<=firstSize:
		out1.write(line)
	else:
		out2.write(line)
	cnt+=1;
	
cnt=0
for line in file2:
	if cnt>firstSize:
		out3.write(line)
	
	cnt+=1
	
file1.close()
file2.close()
out1.close()
out2.close()
out3.close()
