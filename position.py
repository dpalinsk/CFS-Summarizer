
import nltk
import nltk.data



	#position takes in pars and returns a list of tuples of (weight, sentence)
	#pars is an list of pargraphs in the form of a list of tokenized sentences
def position(pars):

	#this will be the list in which we store final weights
	all=[]

	#find number of paragraphs and median paragraph
	sizep = len(pars)
	sizep=sizep-1
	medP=sizep/2
	

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

		#take the tokenized paragraph (pars[x]) then find median (-1 because 0 indexed)
		liste= pars[x]
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
	return all

	
def main():
	pars=[ ["this is a sentence.","here is also a sentence."], ["a yes a sentence for par 2.", "we are in par 2.", "what a dream is par 2"] ]
	print(position(pars)) 	
	

main()
