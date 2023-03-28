

import speech_recognition as sr
from gtts import gTTS
import os
import openai
import pywhatkit as kit

# kit.start_server()

# Initialize OpenAI
openai.api_key = os.getenv('OPEN_AI_KEY')

# Initialize the recognizer
r = sr.Recognizer()


def create_audio_response(text):
    myobj = gTTS(text=text, lang='en', slow=False)
    myobj.save("audio.mp3")
    os.system("mpg321 audio.mp3")


def do_pywhatkit_action(action, text):
    if action == 'play':
        kit.playonyt(text)
    elif action == 'search':
        kit.search(text)


def do_open_ai_prompt(text):
    response = openai.Completion.create(
        engine="davinci",
        prompt=text,
        temperature=0.5,
        max_tokens=50,
    )

    response_text = response['choices'][0]['text']
    print('OpenAI said: ' + response_text)
    create_audio_response(response_text)


while True:
    # Get the microphone input
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)

# Speech recognition using Google Speech Recognition
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        text = r.recognize_google(audio)
        print("You said: " + text)
        create_audio_response(text)
        if 'goodbye' in text:
            create_audio_response("Goodbye")
            break
        elif 'search google' in text:
            text = text.replace("search google", "")
            create_audio_response(f"searching google for {text}")
            do_pywhatkit_action(action="search", text=text)
        else:
            do_open_ai_prompt(text)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        create_audio_response(
            "Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print(
            f"Could not request results from Google \
                    Speech Recognition service; {0}".format(e))
        create_audio_response(
            f"Could not request results from Google Speech Recognition service; {0}".format(e))
# Ask OpenAI a question using the text

# Speak the response
    create_audio_response(response_text)
