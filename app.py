from speech2text import speech2text
# from summarizer_util import summarize_text
from info_extracter import info_extractor
# from google_result import important_link
# from tag_genrator import query_genrator


# step 1: Speech to text [input audio file]
transcribe = speech2text("./audio/chat3.mp3")
print(transcribe)

# Step 2: Use Post tagging to extract information form transcribe [input transcibed text]
points = info_extractor(transcribe)
print(points)


# Step 3: summarize the important points [input important points]
# summarize_text = summarize_text(points)


# Step 4: Get summary tags [input summary of transcibe]
# query = query_genrator(transcribe)
# query = query_genrator(points)


# Step 5:  important links [input keywords]
# links=important_link(query)
