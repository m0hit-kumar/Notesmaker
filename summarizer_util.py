# from summarizer import Summarizer
from gensim.summarization.summarizer import summarize

# model = Summarizer()

test_data = ['This is the title of our course, and the name suggests it all that we are going to do 30 hours of English language that will help you appear more confidently with greater level of competence for those exams that test your English language and your future and your career is shaped or determined by such exam.',
             'By analytical abilities I mean that require contextual kind of reading and understanding complex passages.',
             'So this alone should tell you that how complex the cause and the level of English is going to be here.',
             'Talking about the mode of evaluation you will have continuous assignments Please be serious about that.',
             "So let's use the abridged form of it."]


# def summarize_text(study_notes):
#     body = " ".join(study_notes)
#     # result = model(body, num_sentences=len(study_notes))
#     result = summarize(body, ratio=0.1)
#     return result

print(summarize(test_data[0]))
# print(summarize_text(test_data))
