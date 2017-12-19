
__author__ = 'wegley'

import urllib.request, random

data = urllib.request.urlopen("https://raw.githubusercontent.com/dwyl/english-words/master/words.txt").read()  # read
data = data.split()  # then split it into lines
'''#print it all
for line in data:							#/t this is really great work and i'm honestly impressed, but let me kind of pseudocode how i would do this just for experience sake.
    print(line.decode("utf-8"))'''
'''#gen rand num of lines
sente = random.randint(1,30)				#/t I would first process the list via os.walk and append to create a massive list/vector thing
for x in range(0,sente):
    #stop all the sentences from being in 1 line	#/t if it was a matrix i would import rand and have it generate 2 rand values to output at a time, which would dictate the coordinates of the newly generated word and then deletes it from the list.
    print("\n")
    #generate number of words in sentence			#/t then i would randomize the sentence word count
    words = random.randint(2,20)
    #generate sentence using random line nuumber from text 	#/t then i would generate a newline count, which would then dictate how many sentences + \n combinations would be in my overall 'paragraph' thing
    for m in range(0,words):
        # randomly generate line number to get word			#/t if i was doing matrices for the word bank (which makes it substancially harder) I would also have it try opening the rand coordinate and if else try again. when no further options are available; break the loop.
        line = random.randint(0, 466543)
        sentence = []
        sentence.append(data[line])
        product = b' '.join(sentence)
        print(product.decode("utf-8"), end=' ')'''
#make it gen infinitely
#create initial line number
initline = 466543			#/t make this initline something dynamic that is able to change when the list changes. look into len and glob functions. very useful.
#the loop engine
while initline > 20:
    #stop all the sentences from being in 1 line and print how many terms left
    print(".", initline,"terms left\n")
    #generate number of words in sentence
    words = random.randint(2,20)
    #generate sentence using random line nuumber from text
    for m in range(0,words):
        # randomly generate line number to get word
        line = random.randint(0, initline)
        #init the sentence var
        sentence = []
        #glue words together
        sentence.append(data[line])
        #manage number of words
        del data[line]
        initline = initline - 1
        #compile the sentence
        product = b' '.join(sentence)
        #print
        print(product.decode("utf-8"), end=' ')
#had to hardcode the last "numbers left in list" checkup
print(".", initline,"terms left\n")			#/t hardcoding is a nice band-aid but you should learn how to fix this when you have the time. look into introducing a break into your loop combined with a simple if function
#compile the remaining words in the data
left = b' '.join(data)
print("\n",left.decode("utf-8"), end=" ")	#/t I think this covers most of my complaints i'll reread whenever my coffee is ready; good work and good style, are you just learning off the internet or are you also taking courses?

#/t future topics to play with: get comfortable with input, defining functions and also decoratives. import more python libraries for fun; thats its main advantage
#/t near future programming topic: import time and have it time how long your function has been running.
