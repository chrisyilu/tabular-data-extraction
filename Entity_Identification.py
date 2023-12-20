import nltk
from nltk import word_tokenize, pos_tag, ne_chunk

# Download NLTK resources (run this once)
nltk.download('punkt')
nltk.download('maxent_ne_chunker')
nltk.download('words')


def extract_entities_nltk(text):
    # tokenize the text into words
    words = word_tokenize(text)

    # perform part-of-speech tagging
    pos_tags = pos_tag(words)

    # apply Named Entity Recognition
    named_entities = ne_chunk(pos_tags)

    return named_entities
