# Import necessary libraries
import nltk
import re
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer
from nltk import pos_tag, ne_chunk
from nltk.probability import FreqDist
from nltk.cluster.util import cosine_distance

# Original Text
text = "Apple Inc. is an American multinational technology company headquartered in Cupertino, California that designs, develops, and sells consumer electronics, computer software, and online services. The company's hardware products include the iPhone smartphone, the iPad tablet computer, the Mac personal computer, the iPod portable media player, the Apple smartwatch, and the Apple TV digital media player."

# Tokenization, Removing Stopwords, and Stemming
stop_words = set(stopwords.words("english"))
sentences = sent_tokenize(text)

def preprocess_text(sentence):
    # Remove punctuation characters
    sentence = re.sub(r"[^a-zA-Z0-9]", " ", sentence)
    
    # Tokenization
    words = word_tokenize(sentence)
    
    # Remove stopwords
    filtered_words = [w for w in words if w.lower() not in stop_words]
    
    # Stemming
    stemmer = PorterStemmer()
    stemmed = [stemmer.stem(w) for w in filtered_words]
    
    return stemmed

# Preprocess the sentences
preprocessed_sentences = [preprocess_text(sentence) for sentence in sentences]

# Flatten the list of preprocessed words
flat_preprocessed_words = [word for sentence in preprocessed_sentences for word in sentence]

# Calculate word frequency
word_freq = FreqDist(flat_preprocessed_words)

# Score sentences based on word frequency
def score_sentences(sentences, word_freq):
    sentence_scores = {}
    
    for i, sentence in enumerate(sentences):
        for word in sentence:
            if word in word_freq:
                if i in sentence_scores:
                    sentence_scores[i] += word_freq[word]
                else:
                    sentence_scores[i] = word_freq[word]
    
    return sentence_scores

sentence_scores = score_sentences(preprocessed_sentences, word_freq)

# Generate a summary by selecting top sentences
summary_sentences = []
if sentence_scores:
    sorted_scores = sorted(sentence_scores.items(), key=lambda x: x[1], reverse=True)
    top_sentences = sorted_scores[:3]  # Select the top 3 sentences as the summary
    
    for index, _ in top_sentences:
        summary_sentences.append(sentences[index])

# Join the summary sentences to create the final summary
summary = ' '.join(summary_sentences)

# Print the summary
print("\nSummary:")
print(summary)
