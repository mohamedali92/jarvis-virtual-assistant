import subprocess


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

