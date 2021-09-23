from mdutils import *
import nltk
from nltk.corpus import wordnet
from nltk.corpus import words




word_list = words.words()

for i in word_list:

	mdFile = MdUtils(file_name=i)
	
	synonyms = [] 
	for syn in wordnet.synsets(i):
	    for l in syn.lemmas():
	        synonyms.append(l.name())
	        #if l.antonyms():
	            #antonyms.append(l.antonyms()[0].name())
      
	syndict = (set(synonyms))
	synlist = list(syndict)
	#print(synlist)

	synFormatted = []
	for each in synlist:
		synFormatted.append("[["+each+"]]"+" ")
	synStr = " ".join(str(x) for x in synFormatted)

	mdFile.write("- # Related \n")
	mdFile.write("    - "+synStr)

	mdFile.create_md_file()