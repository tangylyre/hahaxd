import random
wbank = ['u','r','a','butt','i','am','the','boy','we','like','to','scream','u','r','a','butt','i','am','the','boy','we','like','to','scream','u','r','a','butt','i','am','the','boy','we','like','to','scream']
ccap = 10								#have this be a user inputted variable.
def sentencegen (words,hardcap):		#takes a string of words and creates a randomly arranged 'sentence'
	wordcap = len(words)
	sntgen=0
	temprand = 0
	while (wordcap > 1) and (sntgen < hardcap):					#this is giving me problems but i want a blank sentence everytime this loop restarts
		wordcap = len(words)			#wordcap dynamically refreshes per loop which is why its at the beginning
		senlen = random.randint(2,17)	#these are just arbitrary numbers dont worry about it
		inf = False						#inf will activate if hardcap is -1
		die = False						#this basically ends the loop with a break to prevent bugs
		if (wordcap < 17) and (wordcap >1):
			senlen = wordcap
			print("out of words")
			die = True
		while (senlen > 0):				#Will add words until the sentence length value is satisfied
			temprand = random.randint(0,senlen)	#i literally forgot why i set the upper limit to sentence length maybe it makes sense to you
			if (temprand < senlen):
				tempword = words[temprand]
				sntc.append(tempword)
				wordcap =-1
			elif inf is False:
				del words[temprand-1]	#deletion from list should occur if -1 isnt the cap
			senlen =-1					#makes this loop not explode
			sntgen =+ 1					#same
		print(sntc)						#this is doodoo dicks formatting but i could make it look prettier if i had time
		if die is True:
			break						#in case we run out of words this is the break from the loop

sentencegen(wbank,ccap) 				#2 inputs: the actual word bank, and the cap of sentences you want