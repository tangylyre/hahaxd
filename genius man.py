import random
Major = ['A','A#','B','C','C#','D','D#','E','F','F#','G','G#']
cfif=[0,2,4,5,7,9]
calt=[-12,-10,-8,-7,-5,-3]
ckeysval=[1,0,0,1,1,0]
ckeys=["Major","Minor","Minor","Major","Major","Minor"]
y=0
ls=[]
result=""
s = ' '
tempkey=1
root=random.randint(0,11)
for x in range(0,5):
	tempnote=[]
	try:
		tempnote.append(Major[root+cfif[x]])
	except IndexError:
		tempnote.append(Major[root+calt[x]])
	tempnote.append(ckeys[x])
	result = s.join(tempnote)
	ls.append(result)
	x=+1
print (ls)
	
