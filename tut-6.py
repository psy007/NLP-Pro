"""
Chinking
"""


import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer

train_text = state_union.raw("2005-GWBush.txt")
sample_text = state_union.raw("2006-GWBush.txt")
custom_sent_tokenizer = PunktSentenceTokenizer(train_text)
tokenize = custom_sent_tokenizer.tokenize(sample_text)

def process_content():

    for i in tokenize:
        words = nltk.word_tokenize(i)
        tagged = nltk.pos_tag(words)
        chunkGram = r'''Chunk: {<RB.?>*<VB.?>*<NNP>+<NN>?}'''
        chunkParser = nltk.RegexpChunkParser(chunkGram)
        chunked = chunkParser.parse(tagged)
        chunked.draw()



process_content()