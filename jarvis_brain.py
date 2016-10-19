import subprocess

def open_application(app_name):

	def get_list_current_applications():
		p = subprocess.Popen(["ls",  "/Applications/"], stdout=subprocess.PIPE)
		appNames = p.communicate()[0].split("\n")
		return appNames

	def get_app_name(appNamesList, app):
	    for appName in appNamesList:
	        if app in appName.lower():
	            return appName
	    return ""

	current_apps = get_list_current_applications()
	appNameEntered = "sourcetree"
	appName = get_app_name(current_apps, appNameEntered)

	if appName != "":
	    p = subprocess.Popen(["open", "-n", "/Applications/" + appName], stdout=subprocess.PIPE)
	else:
	    print 'No app with that name installed'

	

open_application("bla")