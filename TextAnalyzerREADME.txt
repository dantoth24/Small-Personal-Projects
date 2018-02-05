This project was made with Karen Darken and Carla Naz in December 2016.
This project requires the nltk, as well as some of its addons. Attempting to run the project will prompt you to download the correct files.


THE BASICS: 
	With the help of the Natural Language Toolkit library, we made a program in Python 3.6 that can answer reading comprehension
  questions about text it is given and also generate its own sentences based on user-inputted text. 
How to download the NLTK library: In order to use our program, you must first install the NLTK library. 
Go to this link for instructions: http://www.nltk.org/install.html

***The program will have a default sample text as the program’s input text.***
The program will begin by asking the user what they want to do: analyze the default text (see Part I below), use the sentence generator
(see Part II below), change the text, or exit the script. 

If you decide to change the text, you can only input a text file. The program is set to be able to read documents in the .txt file format.
We will provide a few sample text files for you. For instance, when prompted to provide a text, you can type in “harrypotter.txt” or 
“huckleberryfinn.txt”

Text Analyzer:
	This takes in almost any text (this can range from a few sentences the user has written themselves to a passage from a novel) and a
  question about the text as inputs and outputs a response to the user’s question.
Using the NLTK’s POS tagging, the words of the inputted text are separated into global dictionaries (these dictionaries are called
“subjects”, “verbs”, “objects”, and “adjectives”) based on their respective parts of speech. In these dictionaries, all of the 
relevant words from the text are set as the values to the word’s sentence number. These dictionaries are then used in analyzing 
the words of the question, so the program knows (1) what subjects, verbs, and/or objects the user is asking about and (2) what 
word should look for--given this information, our search functions are able to search for the piece of information the user is
asking for.  Example questions you should try for the default text (“John ate a tasty animal. Betty went to the large store! 
The dog walked to the green park”) include:
What did John do?
What did John eat?
How was the animal?
Where did Betty go?
Was the store large?
Who walked to the park?
Questions of similar format can be asked about any text that is inputted. (If unsure on what you can ask about, while in “analyze” 
mode you can type in “subjects”, “verbs”, “objects”, or “adjectives” to get a list of words that correspond to each part of speech.)
However, the program will not know how to respond to questions that ask what in the text is a certain adjective (for instance, “What
is red?”). Furthermore, this program does not support quotes well; in other words, it isn’t very good at analyzing texts with dialogue.

Sentence Generator:
The sentence generator takes in the inputted text and outputs its own text consisting of sentences that use vocabulary from the
inputted text. The sentence generator knows how to make sentences using 4 of the 5 basic sentence structures including subject-verb,
subject-verb-object, subject-verb-adjective, and subject-verb-noun. We are able to do this because of a script we wrote that utilizes
the NLTK’s POS tagging. The sentence generator randomly selects from these sentence structures to give its outputted texts more variety
and is able to make its outputted texts the same length as its inputted texts using the information it collects about the number of
words, the number of sentences, the average word length, and the average sentence length in the inputted text. 
Because the sentence generator draws from and adds to mutable dictionaries our program creates consisting of the different
types of words in the inputted texts, as the user inputs more text the sentence generator’s vocabulary is expanded. 
The first time the sentence generator is given text, the text must include at least one clear subject, verb, object, 
and adjective or else it will error. If the input text contains quotation marks, make sure the quotation marks are single
quotation marks rather than double quotation marks. 


	Our program is able to identify subjects, verbs, objects, and adjectives in a multi-sentence text. The program can determine a 
  sentence's general format. By manipulating the use of dictionaries, we are able to use a combination of word location, word 
  relationships, and parts of speech (from the NLTK library) to identify if a word resembles one of these criteria and form 
  dictionaries for each indexed by sentence to be used elsewhere in the project. Our program is also able to take in a question
  provided by the user and provide a response.
 The user is able to ask whatever they wish, (with support for “What”, “Where”, etc.) and the program uses its understanding of
 sentences to derive the key information it needs to answer certain word relationship questions the user has about the text. 
 (Asking “Where did John go to eat?” would be interpreted to give an output of objects where John was the subject and eat was
 the verb.) It supports all types of relationships with up to 3 criteria used to find a fourth. Essentially the program narrows
 down what the user is specifically looking for and provide it to them (eg. for “What did John eat?” it would report all objects
 from sentences with John as the subject and ate as the predicate) in an output sentence based on the user's question. The program
 also uses synonyms to better interpret user input question. With the NLTK, we made the program simplify the words of the text 
 and the input question (e.g. “took” would be simplified into “take”) and assess the similarities between the simplified words
 of the text and the simplified words of the user’s questions. By comparing these lists of synonyms and searching for common 
 words, can make sure we find everything that the user is looking for. When combined with the rest of the project this allows
 for some “interpretation, where the program is able to find similar things and not just exactly what the user asks.
 
