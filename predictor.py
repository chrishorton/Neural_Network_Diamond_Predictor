import numpy as np

# First we need to normalize all the data
# "","carat","cut","color","clarity","depth","table","price","x","y","z"
# "1",0.23,"Ideal","E","SI2",61.5,55,326,3.95,3.98,2.43

def contains(bleh, stringToContain):
	for word in bleh:
		if word == stringToContain:
			return True
		else:
			return False

def normalize(file):
	fileData = np.recfromcsv(file)
	quality  = 0
	for line in fileData:
		if contains(line, "Premium"):
			quality = .8
		elif contains(line, "Ideal"):
			quality = 1
		elif contains(line, "Very Good"):
			quality = .6
		elif contains(line, "Good"):
			quality = .4
		elif contains(line, "Fair"):
			quality = .2
		else:
			quality = 0
		print "Quality" + quality

normalize("diamonds.txt")