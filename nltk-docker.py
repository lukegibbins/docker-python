import nltk
import platform

try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

print("\n*** Using NLTK ***\n")

print("- NLTK requires Python versions 2.7, 3.5, 3.6, or 3.7\n")

sentence =  "This python program is running on docker"
print(f"Sentence to tokenize: '{sentence}'")

tokens = nltk.word_tokenize(sentence)
print(f"Tokens in sentence: {tokens}\n")
