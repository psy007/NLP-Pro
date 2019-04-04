"""
Tokenizing word and sentences
1) Tokenizing - word tokenizer ... sentence tokenizer
2) lexicon and corporas
corporas are body of text example- medical journals, presidential speeches, english language etc
lexicons are words and their meaning
investor speak  and regular language speak
investor speak- "bull"---> someone who is positive about the market
english -speak- "bull"--> scary animal you don't want running at you
nltk.download() will download all the necessary packages.
"""

from nltk.tokenize import sent_tokenize, word_tokenize


text = "Hello there, how are you doing today ? The weather is great today and python is awesome. The sky is beautiful"

print(sent_tokenize(text))
print(word_tokenize(text))


