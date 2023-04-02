import requests

API_KEY = "09976f7ca5e2bdb1d939ead7f69a65fab1c09699"
AUDIO_FILE = "./audio/chat3.mp3"

url = "https://api.deepgram.com/v1/listen"
headers = {"Authorization": f"Token {API_KEY}"}


def speech2text(audio_file):
    AUDIO_FILE = audio_file

    with open(AUDIO_FILE, "rb") as f:
        audio_data = f.read()

    response = requests.post(url, headers=headers, data=audio_data)

    if response.ok:
        transcription = response.json()
        result = transcription["results"]["channels"][0]["alternatives"][0]["transcript"]
        print(f"Transcription: {result}")
        return result

    else:
        print(f"Error: {response.status_code} {response.reason}")


# x = speech2text(AUDIO_FILE)
# print(x)
