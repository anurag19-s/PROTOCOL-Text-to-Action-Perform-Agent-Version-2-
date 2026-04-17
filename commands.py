import os
import webbrowser
import subprocess
import datetime
from config import WEBSITES, APPS, FOLDERS


def open_website(site_name: str) -> str:
    site_name = site_name.lower().strip()

    if site_name in WEBSITES:
        webbrowser.open(WEBSITES[site_name])
        return f"Opening {site_name}."

    return f"Website '{site_name}' is not configured."


def open_app(app_name: str) -> str:
    app_name = app_name.lower().strip()

    if app_name in APPS:
        try:
            subprocess.Popen(APPS[app_name], shell=True)
            return f"Opening {app_name}."
        except Exception as error:
            return f"Could not open {app_name}: {error}"

    return f"App '{app_name}' is not configured."


def open_folder(folder_name: str) -> str:
    folder_name = folder_name.lower().strip()

    if folder_name in FOLDERS:
        path = FOLDERS[folder_name]

        if os.path.exists(path):
            os.startfile(path)
            return f"Opening {folder_name} folder."
        return f"Folder path for {folder_name} does not exist."

    return f"Folder '{folder_name}' is not configured."


def get_time() -> str:
    current_time = datetime.datetime.now().strftime("%I:%M %p")
    # include am/pm in the response for clarity
    # use am for times before noon and pm for times after noon and return date as well
    return f"The current time is {current_time} and date is {datetime.datetime.now().strftime('%d %B %Y')}."


def get_date() -> str:
    current_date = datetime.datetime.now().strftime("%d %B %Y")
    return f"Today's date is {current_date}."


def search_google(query: str) -> str:
    query = query.strip()
    if not query:
        return "Please provide something to search on Google."

    url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
    webbrowser.open(url)
    return f"Searching Google for {query}."


def search_youtube(query: str) -> str:
    query = query.strip()
    if not query:
        return "Please provide something to search on YouTube."

    url = f"https://www.youtube.com/results?search_query={query.replace(' ', '+')}"
    webbrowser.open(url)
    return f"Searching YouTube for {query}."


def shutdown_pc() -> str:
    os.system("shutdown /s /t 5")
    return "Shutting down the system in 5 seconds."


def restart_pc() -> str:
    os.system("shutdown /r /t 5")
    return "Restarting the system in 5 seconds."


def cancel_shutdown() -> str:
    os.system("shutdown /a")
    return "Cancelled scheduled shutdown or restart."


def find_best_match(target: str, items: dict) -> str | None:
    target = target.lower().strip()

    if target in items:
        return target

    for name in items:
        if target in name or name in target:
            return name

    return None


def process_command(command: str) -> str:
    command = command.lower().strip()

    if command in ["exit", "quit", "bye"]:
        return "exit"

    if command == "time":
        return get_time()

    if command == "date":
        return get_date()

    if command.startswith("search google "):
        query = command.replace("search google ", "", 1).strip()
        return search_google(query)

    if command.startswith("search youtube "):
        query = command.replace("search youtube ", "", 1).strip()
        return search_youtube(query)

    if command == "shutdown":
        return shutdown_pc()

    if command == "restart":
        return restart_pc()

    if command == "cancel shutdown":
        return cancel_shutdown()

    if command.startswith("open "):
        target = command.replace("open ", "", 1).strip()

        folder_match = find_best_match(target, FOLDERS)
        if folder_match:
            return open_folder(folder_match)

        app_match = find_best_match(target, APPS)
        if app_match:
            return open_app(app_match)

        website_match = find_best_match(target, WEBSITES)
        if website_match:
            return open_website(website_match)

        return f"I do not know how to open '{target}' yet."

    return "Command not recognized."