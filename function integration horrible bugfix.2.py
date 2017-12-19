import glob,os,csv,imp,time
from datetime import datetime
defpath = "C:\\Users\\Yang55\\Pictures\\sample file\\"
out = "C:\\Users\\Yang55\\Pictures\\output\\"
filelst=('.jpg','.png','.gif','.tiff','.tif','.bmp','.fits','.pgm','.ppm','.pbm','.dic','.dcm','.dicom','.pict','.pic','.pct','.psd','.tga')
fgrab=[]
numstr='0'
Roll='10'
Dec='4'
SigM='3'
log=''
def timing(f):
    def wrap(*args):
        time1 = time.time()
        ret = f(*args)
        time2 = time.time()
        print 'Analysis completed at %i images per minute.' % (lim/(time2-time1)*60)
        return ret
    return wrap

def getFile(directory,trgtfiles):
	for file in os.listdir(directory):
		if file.endswith(tuple(trgtfiles)):
			fgrab.append(file);
	lim = len(fgrab);
	if (lim>10):
		SigM='1'
		Dec='2'
		Roll='20'
	return (fgrab, lim);

@timing
def walkAnalysis(fileList,directory,outpath):
	from ij import IJ, ImagePlus
	from ij.macro import Interpreter as IJ1
	from datetime import datetime
	IJ1.batchMode = True
	current=0
	pnum=0
	nooresults=''
	for files in os.walk(directory, topdown=True):
		for file in fileList:
			drc=''.join(directory + file);
			cfile = file
			imp=IJ.open(drc);
			IJ.run("16-bit");										
			IJ.setThreshold(65409, 65532);
			IJ.run("Subtract Background...", "rolling="+Roll+" dark");	##*LIGHT CONDITIONS MUST BE CONSTANT!!* possibly omit light call in order to bugfix
			IJ.run(imp, "Gaussian Blur...", "sigma="+SigM);
			IJ.run("Make Binary"); 									##increases contrast and allows watershed
			IJ.run("Watershed");
			dt = str(datetime.now())[:11]
			savestring=out+"mask"+dt+cfile
			IJ.saveAs(imp, "Jpeg", out+"mask"+cfile);					##jpeg saveas dramatically decreases process time
			IJ.run("Set Measurements...", "integrated area_fraction redirect=None decimal="+Dec);
			IJ.run(imp, "Analyze Particles...", "size=10-Infinity circularity=0.05-1.00 show=[Outlines] display clear include summarize in_situ"); ##most likely the value will change according to desired cell line
			current+=1 												##current is a counter for images processed, as well as possible naming convention for renaming images.
	numstr =str(current);												#current is a int class and cannot be concat with a string.
	dt = str(datetime.now())[:10]										## this slice truncates the colon that is unacceptable in file naming convention. find an alternative solution if possible.
	results= (out+"Results"+dt+".csv");
	if os.path.exists(results):
		while os.path.exists(results):
			pnum +=1
			results = (out+"Results"+dt+'-'+str(pnum)+".csv")	
		IJ.saveAs("Results", results)		
	else:
		IJ.saveAs("Results", results);
	csvStr=(out+"Results"+dt+".csv")
	IJ1.batchMode = False
	return numstr,csvStr;

	
def logVerify(csvstr,count):
	ConF = False
	ConFmsg = ''
	i = []
	j = []
	k = []
	l = []
	log=''
	logdrc= (out+'log'+dt+'.txt')
	cnt=1
	newdrc=''
	if (count !=0):
		with open(csvstr, "r") as f:
			csvreader=csv.reader(f,delimiter = ",")
			csvwriter=csv.writer(f, delimiter= ",")
			next(csvreader, None)		#this skips the header
			for row in csvreader:
				Names = str(row[0])
				AFrac = float(row[4]);
				Count = float(row[1]);
				AvgSize = float(row[3]);
				if (((AFrac+Count)/2)>400) and (AvgSize>170):
						l.append(Names)
				i.append(AFrac);
				j.append(Count);
				k.append(AvgSize);
			if 0 in i:
				log=str("Area fraction is too close to zero, or an error in analysis has occurred. Please manually verify if necesary.\nYour lowest area fraction was: "+str(min(i))+".")
			elif (len(l) != 0):
				ConF = True
				log = str("The following directory was processed: " + defpath + ". \nend batch, "+ numstr +" images processed. \nYour mask images & analysis results are located at: " + out +".")
				if (ConF == True):
					ConFmsg= ("The following listed mask(s) have met the criteria for complete confluence:\n"+'\n'.join(l))
					print("The following listed mask(s) have met the criteria for complete confluence:\n"+'\n'.join(l))
			else:
				log=str("The following directory was processed: " + defpath + ". \nend batch, "+ numstr +" images processed. \nYour mask images & analysis results are located at: " + out +".")
	if os.path.exists(logdrc):
		while (os.path.exists(logdrc)):			
				cnt+=1
				logdrc=(out+'log'+dt+"-"+str(cnt)+'.txt')
		logtxt=open(logdrc, 'w')
	else:
		logtxt=open(logdrc, 'w')
	logtxt.write(log)
	logtxt.write(ConFmsg)
	logtxt.close()
	print log
dt = str(datetime.now())[:10]	
val=getFile(defpath,filelst);
lim=val[1]
walkA=walkAnalysis(fgrab,defpath,out);
numstr=str(walkA[0])
csvStr=str(walkA[1])
logVerify(csvStr,numstr)