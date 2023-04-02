import spacy

# Load the English language model
nlp = spacy.load('en_core_web_sm')

# Preprocess and tokenize the lecture transcript
test_transcript = "This is a sample lecture transcript. It contains multiple sentences."


def info_extractor(transcribed_text):
    data = transcribed_text
    doc = nlp(data)
    sentences = [sent.text for sent in doc.sents]

    # Define the most important parts of speech
    important_pos = ["NOUN", "VERB"]

    # Filter out non-relevant sentences and identify sentences with a clear SVO structure
    important_sentences = []
    for sentence in sentences:
        sentence_doc = nlp(sentence)
        contains_important_pos = any(
            token.pos_ in important_pos for token in sentence_doc)
        is_svo = any(token.dep_ == "nsubj" and token.head.pos_ == "VERB" and any(
            child.pos_ == "NOUN" for child in token.head.children) for token in sentence_doc)

        if contains_important_pos and is_svo:
            important_sentences.append(sentence)

    # Score each sentence based on length and the number of important parts of speech
    def score_sentence(sentence):
        sentence_doc = nlp(sentence)
        length_score = len(sentence.split()) / len(sentences)
        pos_score = sum(
            1 for token in sentence_doc if token.pos_ in important_pos) / len(sentence_doc)
        return length_score + pos_score

    # Rank the important sentences based on their scores
    ranked_sentences = sorted(
        important_sentences, key=score_sentence, reverse=True)

    # Extract the most important sentences
    num_notes = 5
    study_notes = ranked_sentences[:num_notes]

    print(study_notes)
    return " ".join(study_notes)


# info_extractor(test_transcript)
