import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from nltk.chunk import ne_chunk

test_text = "Barack Obama was born in Hawaii and went to Harvard Law School."


def question_detector(transcribe):
    question_words = ["what", "why", "when", "where",
                      "name", "is", "how", "do", "does",
                      "which", "are", "could", "would",
                      "should", "has", "have", "whom", "whose", "don't"]

    question = word_tokenize(question)

    if any(x in question[0] for x in question_words):
        print("This is a question!")
    else:
        print("This is not a question!")


def summary_tag(summary):
    tokens = word_tokenize(summary)
    tagged = pos_tag(tokens)
    entities = ne_chunk(tagged)

    for entity in entities:
        if hasattr(entity, 'label') and entity.label() == 'NE':
            print(entity)

# input transcribe text and summary text


def query_genrator(transcribe):

    # result = transcribe +
    result = summary_tag(transcribe)
    return result
