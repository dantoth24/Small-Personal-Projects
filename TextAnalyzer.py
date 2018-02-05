import nltk
import random 
from nltk.corpus import wordnet
from nltk.stem.wordnet import WordNetLemmatizer
#GLOBAL VARIABLES



sentences={}
subjects={}
verbs={}
origverbs={}
objects={}
adjectives={}
sentences2 = {} #special dictionary for the sentence generator




#FUNCTIONS
def read_file(filename):
  """Returns the text contained in file with given filename."""
  f = open(filename, "r")
  text = f.read()
  return text


def countwords(txt): #counts the number of words in input text
	wordlst = txt.split() 
	return len(wordlst)
def countsens(txt): #counts the number of sentences in input text
	sendic = makesent_for_sengen(txt)
	return sorted(sendic.keys())[-1]
def senlength(txt): #counts the average sentence length in input text
	return round(countwords(txt) / countsens(txt))
def wordlength(txt): #counts the average word length in input text
	wordlst = txt.split() 
	return round(sum(len(word) for word in wordlst) / len(wordlst)) 


def sengenerator(txt): #the actual sentence generator
	analyze_for_sengen(txt)
	i = countsens(txt)
	outputtxt = []
	for x in range(1, i+1):
		senstructure1 = ((random.choice(list(subjects.values()))[:-2]).capitalize() + " " + random.choice(list(verbs.values()))[:-2] + ".")
		senstructure2 = ((random.choice(list(subjects.values()))[:-2]).capitalize() + " " + random.choice(list(verbs.values()))[:-2] + " " + random.choice(list(objects.values()))[:-2] + ".")
		senstructure3 = ((random.choice(list(subjects.values()))[:-2]).capitalize() + " " + random.choice(list(verbs.values()))[:-2] + " " + random.choice(list(adjectives.values()))[:-2] + ".")
		senstructure4 = ((random.choice(list(subjects.values()))[:-2]).capitalize() + " " + random.choice(list(verbs.values()))[:-2] + " " + random.choice(list(subjects.values()))[:-2] + "." or random.choice(list(objects.values()))[:-2] + ".") #NEED NOUN BUT CAN WE DO THAT
		#senstructure5 = (random.choice(list(subjects.values()))[:-2] + " " + random.choice(list(verbs.values()))[:-2] + " " + random.choice(list(adverbs.values()))[:-2] + ".")
		senstructures = [senstructure1, senstructure2, senstructure3, senstructure4]
		chosenstructure = random.choice(senstructures)
		outputtxt.append(chosenstructure + " ")
	sentences2.clear() 
	print ("".join(outputtxt))


def makesent_for_sengen(txt): #makes a dictionary specifically for the sentence generator with each sentence as an entry; each sentence is split into words tagged with their part of speech
	tokens = nltk.word_tokenize(txt) 
	lst = nltk.pos_tag(tokens)  
	i=0
	s=0
	last=0
	for item in lst:
		if item[1] in ['.', ':']:
			s+=1
			sentences2[s]=lst[last:i]
			last=i+1
			i+=1
		else:
			i+=1
	return(sentences2)


def makesent(lst):
	tokens = nltk.word_tokenize(sample)
	lst = nltk.pos_tag(tokens) 
	i=0
	s=0
	last=0
	for item in lst:
		if item[1] in ['.', ':'] :
			s+=1
			sentences[s]=lst[last:i]
			last=i+1
			i+=1
		else:
			i+=1
	return(sentences)


def analyze(txt):
	txt = makesent(txt)
	index=1
	while index<len(txt.keys())+1: #goes through each sentence
		sen=index
		lst=txt[sen]
		i=0
		verbfound=False
		while i<len(lst): #goes through each word
			tup=lst[i]
			pos=tup[1]
			if pos[0]=="N" and verbfound==False:
				subjects[sen]=(tup[0])
			elif pos[0]=="V":
				origverbs[sen]=(tup[0])
				verbfound=True
			elif pos[0]=="N" and verbfound==True:
				objects[sen]=(tup[0])
			elif pos[0]=="J":
				adjectives[sen]=(tup[0])
			else: pass
			i+=1
		index+=1
	for i in list(set(origverbs.keys()).intersection(subjects.keys())).copy():
		verbs[i]=(WordNetLemmatizer().lemmatize(origverbs[i],"v"))
		origverbs[verbs[i]]=origverbs[i]
		origverbs[origverbs[i]]=origverbs[i]
	return([subjects, verbs, objects, adjectives])


def analyze_for_sengen(txt): 
	txt = makesent(txt)
	index=1
	while index<len(txt.keys())+1: #goes through each sentence
		sen=index
		lst=txt[sen]
		i=0
		verbfound=False
		while i<len(lst): #goes through each word
			tup=lst[i]
			pos=tup[1]
			if pos[0]=="N" and verbfound==False:
				subjects[sen]=(tup[0]+".n")
			elif pos[0]=="V":
				verbs[sen]=(tup[0]+".v")
				verbfound=True
			elif pos[0]=="N" and verbfound==True:
				objects[sen]=(tup[0]+".n")
			elif pos[0]=="J":
				adjectives[sen]=(tup[0]+".a")
			else: pass
			i+=1
		index+=1
	return([subjects, verbs, objects, adjectives])


def allsyns(word):
	synonyms = [word]
	for syn in wordnet.synsets(word):
		for l in syn.lemmas():
			synonyms.append(l.name())
	return synonyms #makes list of all synonyms of a word, does not work perfectly for adjectives due to nltk limitations


def search(posin,posout,wordin): #finds synonyms to word from posin(partofspeechin), cuts down posin using the appearance of them, then uses dictionary to locate corresponding output from posout
	wordsyns=allsyns(wordin)
	found=[]
	output=[]
	for item in posin.keys():
		if posin[item] in wordsyns:
			found.append(item)
		else: pass
	for i in list(set(found).intersection(posout)):
		if i > len(posout):
			return False
		output.append(posout[i])
	return output




def search2(posin,posin2,posout,wordin,wordin2): #allows for 2 search parameters
	wordsyns=allsyns(wordin)
	word2syns=allsyns(wordin2)	
	found=[]
	output=[]
	for item in posin.keys():
		if posin[item] in wordsyns:
			found.append(item)
		else: pass
	for i in list(set(found).intersection(posin2)):
		if posin2[i] in word2syns:
			pass
		else: found.remove(i)
	for i in list(set(found).intersection(posout)):
		output.append(posout[i])
	return output


def search3(posin,posin2,posin3,posout,wordin,wordin2,wordin3):#allows for 3 search parameters
	wordsyns=allsyns(wordin)
	word2syns=allsyns(wordin2)
	word3syns=allsyns(wordin3)	
	found=[]
	output=[]
	for item in posin.keys():
		if posin[item] in wordsyns:
			found.append(item)
		else: pass
	for i in list(set(found).intersection(posin2)):
		if posin2[i] in word2syns:
			pass
		else: found.remove(i)
	for i in list(set(found).intersection(posin3)):
		if posin3[i] in word3syns:
			pass
		else: found.remove(i)
	for i in list(set(found).intersection(posout)):
		output.append(posout[i])
	return output #


def word_in_dict(word, dictionary): #is word or any of its synonyms in dictionary?
	found = []
	if word in dictionary.values():
		return True
	else:
		for val in dictionary.values():
			if wordsimilar(word, val) > 0.9:
				return True
	return False


def wordsimilar(word1,word2):
	if word2[0].isupper():
		return False
	if wordnet.synsets(word1)==[] or wordnet.synsets(word2)==[]:
		return False
	w1 = wordnet.synsets(word1)[0]
	w2 = wordnet.synsets(word2)[0]
	output = w1.wup_similarity(w2)
	if output==None:
		return 0
	else:
		return output #provides a value for how similar two words are


def simplify(string):
	string=nltk.word_tokenize(string)
	temp=""
	for item in string:
		if item in [".","?","!","What","When","Where","Did","Who","did","do","Was","How","was","Do"] or nltk.pos_tag([item])[0][1] in ["DT", "IN", "TO"]:
			pass
		else:
			temp=temp+" "+WordNetLemmatizer().lemmatize(item,"v")
	return temp #simplifies a string to remove articles, etc.


def analyze_ques(question): #takes an input question and responds by combining most of the other funtions
	if question=="subjects":
		return subjects
	elif question=="verbs":
		return verbs
	elif question=="objects":
		return objects
	elif question=="adjectives":
		return adjectives
	ques_words = nltk.word_tokenize(question)
	qword= ques_words[0]
	squestion = simplify(question)
	ques_loop = nltk.word_tokenize((squestion))
	if qword=="Did" or qword == "What":
		for item in ques_loop:
			if item in adjectives.values():
				ques_loop.remove(item)
	qlength = len(ques_loop)
	wordin={}
	for i in range(1,4):
		wordin[i]=''
		origverbs[wordin[i]]=''
	found={}
	n=1
	i=1
	for word in ques_loop:
		if word_in_dict(word, subjects):
			wordin[i] = word
			found[i]=subjects
			i+=1
		elif word_in_dict(word, verbs):
			wordin[i] = word
			found[i]=verbs
			i+=1
		elif word_in_dict(word, objects):
			wordin[i] = word
			found[i]=objects
			i+=1
		elif word_in_dict(word, adjectives):
			wordin[i] = word
			found[i] = adjectives
			i+=1
		else:
			pass
	if "Who" in ques_words:
		found[len(found)+1]=subjects
	elif not(set(ques_words).isdisjoint(["What","Did","did","Where"])):
		if found[len(found)]==verbs:
			found[len(found)+1]=objects
		else: 
			found[len(found)+1]=verbs
	elif not(set(ques_words).isdisjoint(["Was","How","was"])):
		found[len(found)+1]=adjectives
	else:
		found[len(found)+1]=found[2]
	if wordin[1] =='':
		analyzed= False
	elif wordin[2] =='':
		if qlength>(1):
			analyzed= False
		else:
			analyzed= search(found[1],found[2],wordin[1])
	elif wordin[3] =='':
		if qlength>(2):
			analyzed= False
		else:
			analyzed= search2(found[1],found[2],found[3],wordin[1],wordin[2])
	else:
		if qlength>(3):
			analyzed= False
		else: 
			analyzed= search3(found[1],found[2],found[3],found[3],wordin[1],wordin[2],wordin[3])
	return(output_text(analyzed, wordin,qword ))


def output_text(analyzed, wordin,qword,):#takes these inputs inside analyze_ques to make an output sentence based on question
	output=[]
	if analyzed==False or analyzed==[]:
		if qword == "What":
			output.append(wordin[1])
			output.append("did not")
		elif qword == "Who":
			return("No one.")
		elif qword == "How":
			return("Nothing special.")
		elif qword == "Where":
			return("Nowhere.")
		else:
			return("No.")
	else:
		if analyzed[0] in verbs.values():
			for item in analyzed.copy():
				analyzed.append(origverbs[item])
				analyzed.remove(item)
		if qword == "What":
			output.append(wordin[1])
			output.append(origverbs[wordin[2]])
			output.append(' and '.join(analyzed))
		elif qword == "Who":
			output.append(' and '.join(analyzed))
			output.append(origverbs[wordin[1]])
			output.append(wordin[2])
			output.append(wordin[3])
		elif qword == "How":
			output.append(wordin[1])
			output.append("was")
			output.append(' and '.join(analyzed))
		elif qword == "Where":
			output.append("To")
			output.append(' and '.join(analyzed))
		else:
			output.append('Yes')
	if not output[0][0].isupper():
		output.insert(0,output[0].title())
		output.remove(output[1])
	for item in output.copy():
			if item=='':
				output.remove(item)
	return(' '.join(output)+'.')


#PROJECT CODE


ask=input('Do you want to change the input text, or use the default? ')
if "change" in ask or "input" in ask or "text" in ask:
	sample = read_file(input(' Okay, input the filename of the text you want to ask about here: '))
	print("Thank you!")
	print('CURRENT TEXT:'+'['+sample+']')
else:
	sample = "John ate a tasty animal. Betty went to the large store! The dog walked to the green park."
	print("Okay, using the default sample.")
	print(' CURRENT TEXT:'+'['+sample+'] ')
repeat=True
while repeat==True:

	query=input(" Do you want to analyze this text, use sentence generator, get help, or exit? ")
	query=nltk.word_tokenize(query)
	if "analyze" in query:
		analyze(sample)
		check=True
		while check==True:
			user_q = input(' Ask a question about the text, or type back to go back. ')
			if user_q == "back":
				check = False
			if not(user_q == "back"):
				print(analyze_ques(user_q))
	elif "sentence" in query or "generator" in query:
		analyze(sample)
		print("Generating sentences...")
		print(sengenerator(sample))
	elif "exit" in query:
		repeat=False
	elif "help" in query:
		print(" Analyzing text allows you to input certain questions beginning with Who, What, Where, How(for asking about a nouns traits), or Was(Same as How). It will then tell you the information you ask about. The sentence generator will generate a random sentence seeded from the current text. Changing the input texts lets you run this program on the text from any text file. ")
	else:
		print(" Error, try a different response, or typle help for help. ")
	




