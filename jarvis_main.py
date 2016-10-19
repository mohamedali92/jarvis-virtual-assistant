from jarvis_speak import speak
from jarvis_listen import listen
import jarvis_brain


speak("What can I do for you Sir?")
request = listen()
if "open" in request:
	jarvis_brain.open_application(request.split("open ")[1])
elif "weather" in request:
	city = str(request.split("in ")[1])
	result = jarvis_brain.get_weather(city)
	speak(result)
