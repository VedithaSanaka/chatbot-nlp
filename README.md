NLP-Based Question Answering Chatbot

This project demonstrates a simple but powerful chatbot built using Python and NLP techniques. It processes a dataset of question-answer pairs 
to enable intelligent and flexible answering based on user input.

Features :
Reads a dataset of questions and answers from a CSV file.

Applies full NLP preprocessing: tokenization, stopword removal, POS tagging, and lemmatization.

Converts each question into a keyword signature for effective matching.

Accepts user input in natural language and returns the most relevant answer based on processed keywords.

Uses a pipeline-based approach for training and response generation.

Dataset Structure :
The dataset should be a CSV file with two columns:

question: The natural language question.

answer: The answer corresponding to the question.

Technologies Used :

Python
Pandas
NLTK
CSV for dataset storage
Streamlit
