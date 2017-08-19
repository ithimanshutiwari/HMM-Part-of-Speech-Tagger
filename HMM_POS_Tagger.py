from collections import Counter

#Following function open output file for writing word tag sequence. 
o1=open('output','w')


# Possible Tag Finder for HMM Tagger
def possibleTagFinder(s,l):
	tag=[]
	for j in l:
		for i in s:
			if(i==j[0]):
				tag.append(j[1])
	return tag



#Creation of dictionary for tagged word and for tag
l=[]
z=[]
x=[]
with open('tagged_brown_corpus') as fp:
    for line in fp:
        splitArr=line.split(" ")
        for i in splitArr:
        	o=i.split("_")
        	if len(o)>1:
			if o[1].split()[0] in ('.|SB01:1','.|SC01:1','.|SD01:1','.|SE01:1','.|SF01:1','.|SG01:1','.|SH01:1','.|SJ01:1','.|SK01:1','.|SL01:1','.|SM01:1','.|SN01:1','.|SP01:1','.|SR01:1'):
				l.append((o[0],'.'))
				z.append(o[0]+'_.')
				x.append('.')
			else:
				l.append((o[0],o[1].split()[0]))    
				z.append(o[0]+'_'+o[1].split()[0])
				x.append(o[1].split()[0])

dict_tagged_word =Counter(z)
dict_tag=Counter(x)
string_tag=''.join(x)



#Automatic Execution of Viterbi on untagged brown corpus 
with open('untagged_brown_corpus') as f:
    for line in f:
	s=line.split()	# Input Text String
	if len(s)==0:
		continue
	tag=possibleTagFinder(s,l)
	tag=list(set(tag))	# Unique Tag Estimation

	if len(tag)==0:
		tag.append('NP')

	
	#Transition Table Estimation
	transition=[[0 for i in xrange(len(tag))] for j in xrange(len(tag)+1)]
	for i in xrange(len(tag)):
		transition[0][i]=float(dict_tag[tag[i]])/len(l)
	for i in range(1,len(tag)+1):
		for j in range(len(tag)):
			transition[i][j]=float(string_tag.count(tag[i-1]+tag[j]))/dict_tag[tag[i-1]];


	#Observation Table Estimation
	observation=[[0 for i in xrange(len(s))] for j in xrange(len(tag))]
	for i in range(len(tag)):
		for j in range(len(s)):
			observation[i][j]=dict_tagged_word[s[j]+"_"+tag[i]]
	
	
	#Viterbi algorithm to implement HMM Tagger
	def viterbi(w,t,a,b):
		v=[[0 for i in xrange(t)] for j in xrange(w)]
		back=[0 for i in xrange(w+1)]
	
		for s in range(t):
			v[0][s]=a[0][s]*b[s][0]
		
		for w1 in xrange(1,w):
			for t1 in xrange(t):
				m=0
				for t2 in xrange(t):
					if (v[w1-1][t2]*a[t2+1][t1]*b[t1][w1])>m:
						m=v[w1-1][t2]*a[t2+1][t1]*b[t1][w1]
				v[w1][t1]=m+1;
			back[w1]=v[w1-1].index(max(v[w1-1]))

		m=0
		for t2 in xrange(t):
			if (v[w-1][t2])>m:
				m=(v[w-1][t2])
			
		back[w]=v[w-1].index(max(v[w-1]))
		return back
	
			
	back=viterbi(len(s),len(tag),transition,observation)
	for i in xrange(1,len(back)):
		# Write output on console
		print s[i-1]+"_"+tag[back[i]]
		#Write to the output file
		o1.write(s[i-1]+"_"+tag[back[i]]+" ")
	o1.write("\n");
			

		

