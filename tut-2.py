"""
Stop Words are commonly used word
stop word filtration for removing stop  words
"""

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

text = "This is an example showing stop word filtration"
stopwords = set(stopwords.words("english"))
words = word_tokenize(text)
filtered_word = []

# for w in words:
#     if w not in stopwords:
#         filtered_word.append(w)
#
# print(filtered_word)

filtered_word = [w for w in words if w not in stopwords]

print(filtered_word)