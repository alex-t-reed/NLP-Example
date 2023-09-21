# Import necessary libraries
import nltk  # Natural Language Toolkit for text processing
import re    # Regular expressions for text cleaning
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords  # Stopwords for text filtering
from nltk.stem.porter import PorterStemmer  # Stemming
from nltk.stem.wordnet import WordNetLemmatizer  # Lemmatization
from nltk import pos_tag, ne_chunk  # Part of speech tagging and named entity recognition

# Original Text
text = "Apple Inc. is an American multinational technology company headquartered in Cupertino, California that designs, develops, and sells consumer electronics, computer software, and online services. The company's hardware products include the iPhone smartphone, the iPad tablet computer, the Mac personal computer, the iPod portable media player, the Apple smartwatch, and the Apple TV digital media player."

# Print the original text
print("Original Text:")
print(text)

# Tokenization
sentences = sent_tokenize(text)
print("\nTokenized Sentences:")
print(sentences)

# First sentence
print("\nFirst Sentence:")
print(sentences[0])

# Remove punctuation characters from the first sentence
# Explanation: r"[^a-zA-Z0-9]" means match any character that is NOT a letter (lowercase or uppercase) or a digit (0-9).
# The replacement " " replaces the matched characters with a space.
text = re.sub(r"[^a-zA-Z0-9]", " ", sentences[0])
print("\nText after Punctuation Removal:")
print(text)

# Tokenization
words = word_tokenize(text)
print("\nTokenized Words:")
print(words)

# Removing stop words
stop_words = set(stopwords.words("english"))
filtered_words = [w for w in words if w not in stop_words]
print("\nWords after Stopword Removal:")
print(filtered_words)

# Stemming
stemmer = PorterStemmer()
stemmed = [stemmer.stem(w) for w in filtered_words]
print("\nStemmed Words:")
print(stemmed)

# Lemmatization
lemmatizer = WordNetLemmatizer()
lemmatized = [lemmatizer.lemmatize(w) for w in filtered_words]
print("\nLemmatized Words:")
print(lemmatized)

# Part of speech tagging
tagged_words = pos_tag(filtered_words)
print("\nPart of Speech Tags:")
print(tagged_words)

# Named entity recognition
ner_tree = ne_chunk(pos_tag(word_tokenize(sentences[0])))
print("\nNamed Entity Recognition:")
print(ner_tree)
