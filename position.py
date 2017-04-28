
import nltk
import nltk.data

def main():
	#the following code is to deal with opening/reading text files can be deleted later on
	text=open("text.txt", 'r')
	lines= text.readlines()
	#this separates the file into paragraphs and puts it into the array pars. 
	pars=[]
	for line in lines:
		if "\n" in line:
			if line!="\n":
				pars.append(line)

	#this opens the english tokenizer from nltk
	tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
	
	#resets the file to the beginning so the tokenizer can use it.
	text.seek(0)
	whole = text.read()

	#all<=tuple array of format (weight, sentence)
	all=[]
	
	#find number of paragraphs and median paragraph
	sizep = len(pars)
	sizep=sizep-1
	medP=sizep/2

	print("median par number= ", medP)
	#for each paragraph in file find the median line indice and then define pweight (paragraph weight) based of that
	for x in range(0,len(pars)):

		size1=len(pars)
		pweight=1
		
		if x>medP:
			pweight=x-medP
			pweight=pweight/size1
			pweight= 1-pweight

		elif x<medP:
			pweight=medP-x
			pweight=pweight/size1
			pweight=1-pweight

		print(medP)
		print("PAR START-------------  ", pweight, ", ", x)		
		#tokenize the sentences in paragraph, then find median (-1 because 0 indexed)
		liste= tokenizer.tokenize(pars[x])
		numS= float(len(liste)-1)
		median= float(numS/2)

		#for each senence in paragraph, set sentence weight (sweight) 
		#then define total weight to be (0.5)(sweight+ pweight). This weight sentence position and par position equally
		#but we could probably change it if need be.
		for elt in liste:
			ind= float(liste.index(elt))
			sweight=1
			#if length of paragraph is 1 sentence. Set sweight to 1.
			if len(liste)==1:
				sweight=1
				weight=0.5*(sweight+pweight)
				all.append((weight,elt))
			else:	
				#the weight of the sentence is defined by how far it is away from the median.
				#the farther away, the higher the weight. Because topic senetences and concluding
				#sentences tend to be more informationally important
				sweight=0
				weight=0
				if ind<=median:
					test=median-ind
					test=test/numS
					sweight=test
					weight=0.5*(sweight+pweight)
				else:
					test= ind-median
					test=test/numS
					sweight=test
					weight=0.5*(sweight + pweight)
				all.append( (weight, elt))
			print("weight, sweight, pweight, elt:   ", weight, sweight, pweight, elt)



	
	
	

main()
