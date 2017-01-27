from nltk.corpus import stopwords
sw = stopwords.words("english")
print len(sw) #153 stopwords in english language

from nltk.stem.snowball import SnowballStemmer
stemmer = SnowballStemmer("english")
print stemmer.stem("responsiveness")	# respons
print stemmer.stem("responsivity")		# respons
print stemmer.stem("unresponsive")		# unrespons




