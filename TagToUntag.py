o1=open("untagged_brown_corpus",'w')
out=""
with open("tagged_brown_corpus") as fp:
	for i in fp:
		for j in i.split():
			k=j.split("_")
			out+=k[0]+" "
			
		out+="\n"
	print out
o1.write(out)
o1.close()
