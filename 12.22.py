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
outfile=str("C:/Users/Yang55/Downloads/Progression.txt")
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
	try:
		twrite=open(outfile, 'w')
	except PermissionError:
		print("looks like there was a permission error: skipping log file")
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
		twrite.write('root note randomized\n')
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
		twrite.write('chord count randomized\n')
		chrct = random.randint(3,10)
	if int(chrct) > 1:
		for n in range (1,int(chrct)):
			prog.append(ls[random.randint(0,5)])
	elif int(chrct) == 1:
		temprand = random.randint(1,3)
		print((dict[temprand])[0])
		twrite.write((dict[temprand])[0]+'\n')
		for n in range(1,len(dict[temprand])):
			prog.append(ls[(dict[temprand])[n]])
	elif int(chrct) < 1:
		for n in range (0,6):
			prog.append(ls[n])
	print ('[%s]' % ', '.join(map(str, prog)))
	twrite.write('[%s]' % ', '.join(map(str, prog))+'\n')
	twrite.close()
	return prog
	
def scalegen(prog):
	
	semitone = ['A','A#/Bb','B','C','C#/Db','D','D#/Eb','E','F','F#/Gb','G','G#/Ab']
	majmod = [0,2,4,5,7,9,11]
	majalt = [0,-10,-8,-7,-5,-3,-1]
	minmod = [0,2,3,5,7,8,10]
	minalt = [0,-10,-9,-7,-5,-4,-2]
	Tonic=''
	Supertonic=''
	Mediant=''
	Subdominant=''
	Dominant=''
	Supermediant=''
	Leading=''
	tempscale=[]
	keys = {1:majmod,
			2:majalt,
			3:minmod,
			4:minalt}
	degrees = {	0:Tonic,
				1:Supertonic,
				2:Mediant,
				3:Subdominant,
				4:Dominant,
				5:Supermediant,
				6:Leading	}
	for x in range(0,len(prog)):
		try:
			twrite=open(outfile, 'a')
		except PermissionError:
			pass
		twrite.write(prog[x]+'\n')
		tempscale=[]
		if ("Major" in prog[x]):
			k = 1
		elif ("Minor" in prog[x]):
			k = 3
		for n in range(0,11):
			if (semitone[n] == (prog[x])[:1]):
				root = n
				if "#" in semitone[n]:
					root =+ 1
				for j in range (0,6):
					try:
						degrees[j] = semitone[root + (keys[k])[j]]	
					except IndexError:
						k = k+1
						degrees[j] = semitone[root + (keys[k])[j]]
					tempscale.append(degrees[j])
		print ("the following scale is in the key of "+prog[x]+":")
		print ('[%s]' % ', '.join(map(str, tempscale)))
		def basstranscribe(scalels):
			semitone = ['A','A#/Bb','B','C','C#/Db','D','D#/Eb','E','F','F#/Gb','G','G#/Ab']
			Estring = 7
			Astring = 0
			Dstring = 5
			Gstring = 10
			tnote = 0
			chordbox = []
			Gls=[]
			Dls=[]
			Als=[]
			Els=[]
			stringmaps = ("","G String", "D String", "A String", "E String")
			strings ={	1:Gstring,
						2:Dstring,
						3:Astring,
						4:Estring}
			stls={	1:Gls,
					2:Dls,
					3:Als,
					4:Els}
			for note in scalels:
				Gls=[]
				Dls=[]
				Als=[]
				Els=[]
				for notenum in range(0,len(semitone)):
					if (semitone[notenum] == note):
						tnote = notenum
						for string in range (1,5):			#if you're partial to hitting not hitting some bass strings..
							chordbox=[]
							for x in range (0,24):		#change the range to choose preferences (ie playing on the neck)
								if (((strings[string] + x)%12)==tnote):
									chordbox.append(x)
									stls[string].append(x)
									stls[string].sort()
			for string in range(1,5):
				twrite=open(outfile, 'a')
				templs=stls[string]
				prev = 0
				printls=[]
				if ((stls[string])[0])!=0:
					printls.append('-')
				for num in stls[string]:
					if num != '-':
						cur = num
						diff = cur-prev
						if diff > 0:
							for x in range(1,diff):
								printls.append('-')
						prev = cur
						printls.append(num)
				twrite.write(('[%s]' % ', '.join(map(str, printls)))+'\n')
		twrite.close()
		basstranscribe(tempscale)	
prog = proggen(Uinput,Chordct)
scalegen(prog)
print("A transcription of your scales is located at: "+outfile+".")