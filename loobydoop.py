turn = ("Turnaround",0,5,1,4)
circle = ("Circle Progression",5,1,4,0)
atebar = ("Eight-bar Blues (Use 7th chords!)",0,4,3,3,0,4,3,1,4)
twelver = ("Twelve-bar Blues (Mix in some 7ths!)",0,3,0,0,3,3,0,0,4,3,0,0)
sprog = ("Sensitive Female Progression",5,3,0,4)
fiddy = ("50's progression (Doo-wop maybe?)",0,5,3,4)
toofi = ("ii-V-I (jazz harmony?)",1,4,0)
dict = {1:turn,
		2:circle,
		3:atebar,
		4:twelver,
		5:sprog,
		6:fiddy,
		7:toofi,}
outfile=str("C:/Users/Yang55/Downloads")
import random, csv, os
print("Enter a major or (m)inor chord to generate a circle of fifths progression, no flats and no need to label major chords!")
print("ex: F#m, G#, and E are all valid forms. Gbma, Eb, and Cmaj are not valid forms.")
Uinput = input("Write anything else for a randomized root note!\n: ")
print("Enter the amount of chords you want in your progression!\nEnter 0 to map the entire circle!\nenter 1 to choose from a bank of common progressions!")
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
		except IndexError or TypeError:
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
		chrct = random.randint(3,10)
	if int(chrct) > 1:
		for n in range (1,int(chrct)):
			prog.append(ls[random.randint(0,5)])
	elif int(chrct) == 1:
		temprand = random.randint(1,3)
		print((dict[temprand])[0])
		for n in range(1,len(dict[temprand])):
			prog.append(ls[(dict[temprand])[n]])
	elif int(chrct) < 1:
		for n in range (0,6):
			prog.append(ls[n])
	print ('[%s]' % ', '.join(map(str, prog)))
	try:
		twrite=open(outfile, 'w')
		twrite.write('[%s]' % ', '.join(map(str, prog)))
		twrite.close()
	except PermissionError:
		print("looks like there was a permission error: please use administrator access in order to save a log file please!")
proggen(Uinput,Chordct)