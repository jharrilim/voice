import speech_recognition as sr


def listen(recog: sr.Recognizer):
    with sr.Microphone() as source:
        print('Speak: ')
        audio = recog.listen(source=source, phrase_time_limit=5000)
        print('Time is up')
    return audio


if __name__ == '__main__':
    recog = sr.Recognizer()
    audio = listen(recog)
    try:
        print('Recorded: ' + recog.recognize_google(audio))
    except Exception as e:
        print(e)

