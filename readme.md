# NLP Examples: Preprocessing and Extractive Summarization

Two Python learning scripts showing a text-processing pipeline with NLTK. This is the foundation of my related summarization projects, rather than a separate production product.

## Scripts

- `NLP_Text_Preprocessing.py`: sample text, sentence/word tokenization, stopword removal, stemming, lemmatization, tagging, and named-entity recognition.
- `TextSummarization_Preprocess.py`: frequency-based sentence scoring and extractive summarization.

## Run locally

Use a virtual environment compatible with the older versions in `requirements.txt`:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m nltk.downloader punkt stopwords wordnet omw-1.4 averaged_perceptron_tagger maxent_ne_chunker words
python NLP_Text_Preprocessing.py
python TextSummarization_Preprocess.py
```

The scripts use sample text in their source; edit that text to experiment. NLTK data is downloaded separately from Python packages. Resource names can differ across NLTK versions; follow any missing-resource message if updating the environment.

## Related work

- [Text Summarizer + Sentiment Analysis](https://github.com/alex-t-reed/Text-Summarizer-Sentiment-Analysis): Flask interface using frequency scoring and TextBlob.
- [Thought Summarizer](https://github.com/alex-t-reed/Thought-Summarizer): separate transformer-based experiment.

These approaches have different tradeoffs. Word-frequency scoring extracts existing sentences and does not guarantee that the most important meaning is retained. The scripts are educational examples, not trained domain-specific NLP systems.

## About and contact

Created by [Alex Reed](https://www.linkedin.com/in/alextreed/). Explore my [portfolio](https://alex-t-reed.github.io/) for project context and career interests. Professional inquiries are welcome through LinkedIn.

## What I learned

I practiced breaking text processing into inspectable steps: tokenization, filtering, linguistic normalization, and sentence scoring. Comparing the intermediate outputs helped me understand how preprocessing choices affect the final result.
