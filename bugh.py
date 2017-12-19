import random
print("Enter a major or (m)inor chord to generate a circle of fifths progression, no flats and no need to label major chords!")
print("ex: F#m, G#, and E are all valid forms. Gbma, Eb, and Cmaj are not valid forms.")
Uinput = input("Write anything else for a randomized root note!\n: ")
print("Enter the amount of chords you want in your progression!")
Chordct = input("Write any non-int to have a randomly generated progression!\n")
def proggen(rootchr,chrct):
	Major = ['A','A#','B','C','C#','D','D#','E','F','F#','G','G#']
	Minor = ['Am','A#m','Bm','Cm','C#m','Dm','D#m','Em','Fm','F#m','Gm','G#m']
	cfif=[0,2,4,5,7,9]
	calt=[-12,-10,-8,-7,-5,-3]
	ckeysval=[1,0,0,1,1,0]
	ckeys=["Major","Minor","Minor","Major","Major","Minor"]
	numchord = ["I","ii","iii","IV","V","vi"]
	y=0
	ls=[]
	result=""
	s = ' '
	tempkey=1
	prog=[]
	if rootchr in Major:
		for x in range(0,11):
			if (Major[x] == rootchr):
				rootchr = x
	elif rootchr in Minor:
		for x in range(0,11):
			if (Minor[x] == rootchr):
				try:
					rootchr = x + 3
				except IndexError:
					rootchr = x - 9
	else:
		print("randomizing root note...\n")
		rootchr=random.randint(0,11)
	for x in range(0,6):
		tempnote=[]
		try:
			tempnote.append(Major[rootchr+cfif[x]])
		except IndexError:
			tempnote.append(Major[rootchr+calt[x]])
		tempnote.append(ckeys[x])
		tempnote.append("("+numchord[x]+")")
		result = s.join(tempnote)
		ls.append(result)
		x=+1
	try:
		int(chrct)
	except ValueError or TypeError:
		print('randomizing chord count...')
		chrct = random.randint(1,10)
	prog.append(ls[0])
	for n in range (1,int(chrct)):
		prog.append(ls[random.randint(0,5)])
	print ('[%s]' % ', '.join(map(str, prog)))
	
proggen(Uinput,Chordct)