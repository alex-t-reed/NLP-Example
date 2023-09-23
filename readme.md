# NLP-Example Repository

This repository contains two Python scripts for Natural Language Processing (NLP) tasks and text summarization, as well as a requirements.txt file specifying the necessary dependencies. Read the tutorials on Medium here:

[Writing Your First NLP Python Script: From Text Preprocessing to Named Entity Recognition](https://medium.com/@alexreed.atr/a3eb71f5b2f?source=friends_link&sk=202e9690591868f22a142ef4ddc8bd38)
[Creating a Text Summarization Tool in Python using NLP](https://medium.com/@alexreed.atr/58fa7aa54b66?source=friends_link&sk=7706cb1ad4d4fce60074c5ca25b336bd)

## What is Natural Language Processing (NLP)?

Natural Language Processing (NLP) is a field of artificial intelligence that focuses on the interaction between computers and human language. It involves the development of algorithms and models that enable computers to understand, interpret, and generate human language text. NLP has a wide range of applications, including text classification, sentiment analysis, machine translation, and text summarization.

## Why This Repository?

This repository was created to provide practical examples of NLP techniques implemented in Python. The scripts included here demonstrate how to perform common NLP tasks such as text preprocessing, tokenization, removing stopwords, stemming, and text summarization. These scripts can serve as a starting point for individuals interested in learning about NLP or incorporating NLP into their projects.


## Files:

1. **NLP_Text_Preprocessing.py**
   - This script demonstrates various text preprocessing techniques using the Natural Language Toolkit (NLTK) library.
   - It covers tokenization, removing stopwords, stemming, and more.
   
2. **TextSummarization_Preprocess.py**
   - This script builds on the previous one and adds a text summarization component.
   - It uses word frequency to score sentences and generates a summary from the input text.

## Requirements:

To run the scripts in this repository, make sure you have the following dependencies installed:

click==8.1.7
joblib==1.3.2
nltk==3.8.1
numpy==1.26.0
regex==2023.8.8
tqdm==4.66.1

You can install these dependencies using `pip` by running the following command:

```bash
pip install -r requirements.txt
```

## How to Run the Code:
1. Clone this repository to your local machine using Git:
```bash
git clone https://github.com/alex-t-reed/NLP-Example.git
```

2. Navigate to the repository directory:

```bash
cd NLP-Example
```

3. Install the required dependencies as mentioned above.

4. Run the desired Python script:

To run the NLP text preprocessing script, use:
```bash
python NLP_Text_Preprocessing.py
```

To run the text summarization script, use:
```bash
python TextSummarization_Preprocess.py
```
---
## Feedback:

For questions, suggestions, or collaboration opportunities, please don't hesitate to reach out me.
- **Email**: [Alex Reed](mailto:alexreed@ucsb.edu)
- **LinkedIn**: [Alex Reed on LinkedIn](https://www.linkedin.com/in/alextreed)

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/alextreed)

Feel free to explore the scripts and use them for your NLP tasks. If you have any questions or suggestions, don't hesitate to reach out through LinkedIn or by creating an issue in this repository.