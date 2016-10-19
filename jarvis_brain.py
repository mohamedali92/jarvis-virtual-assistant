import subprocess
import pyowm


def open_application(app_name):

    def get_list_current_applications():
        p = subprocess.Popen(["ls",  "/Applications/"], stdout=subprocess.PIPE)
        app_names = p.communicate()[0].split("\n")
        return app_names

    def get_app_name(current_apps, app):
        for existing_app in current_apps:
            if app in existing_app.lower():
                return existing_app
        return ""

    current_installed_apps = get_list_current_applications()
    true_app_name = get_app_name(current_installed_apps, app_name)

    if true_app_name != "":
        p = subprocess.Popen(
            ["open", "-n", "/Applications/" + true_app_name], stdout=subprocess.PIPE)
    else:
        print 'No app with that name installed'
def get_weather(city):
	owm = pyowm.OWM('9a52c132091aca0a2566d332ec00474d')  # You MUST provide a valid API key

	# Search for current weather in city
	observation = owm.weather_at_place(city)
	w = observation.get_weather()
	temp = w.get_temperature('celsius')['temp']  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
	result_phrase =  "The temperature in " + city + " is: " + str(temp) + " Celcius"
	print result_phrase
	return result_phrase


