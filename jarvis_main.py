from os import system
import speech_recognition
import jarvis_brain

recognizer = speech_recognition.Recognizer()

def speak(text):
	system('say '+text)

def listen():
	with speech_recognition.Microphone() as source:
		recognizer.adjust_for_ambient_noise(source)
		speak("What can I do for you Sir?")
		audio = recognizer.listen(source)
	try:
	    # for testing purposes, we're just using the default API key
	    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
	    # instead of `r.recognize_google(audio)`
	    #print("Google Speech Recognition thinks you said " + recognizer.recognize_google(audio))
	    text = recognizer.recognize_google(audio)
	    jarvis_brain.speak()
	    print (text)
	    speak(text)
	except speech_recognition.UnknownValueError:
	    print("Google Speech Recognition could not understand audio")
	except speech_recognition.RequestError as e:
	    print("Could not request results from Google Speech Recognition service; {0}".format(e))


listen()