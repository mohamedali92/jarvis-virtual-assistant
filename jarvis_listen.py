import speech_recognition

recognizer = speech_recognition.Recognizer()


def listen():
	with speech_recognition.Microphone() as source:
		recognizer.adjust_for_ambient_noise(source)
		audio = recognizer.listen(source)
	try:
	    # for testing purposes, we're just using the default API key
	    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
	    # instead of `r.recognize_google(audio)`
	    #print("Google Speech Recognition thinks you said " + recognizer.recognize_google(audio))
	    text = recognizer.recognize_google(audio)
	    print text
	    return text
	except speech_recognition.UnknownValueError:
	    print("Google Speech Recognition could not understand audio")
	except speech_recognition.RequestError as e:
	    print("Could not request results from Google Speech Recognition service; {0}".format(e))
