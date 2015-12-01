#!/usr/bin/env python
import time
from time import gmtime, strftime
import commands
import random

sleep_time = 60*76 #sleep for 76 minutes
start_hour = 10
end_hour = 18

def run_command(command):
    commands.getstatusoutput(command)

def mini_windows():
    command = "osascript -e 'activate application \"Finder\"' -e 'tell application \"System Events\"' -e 'set visible of processes where name is not \"Finder\" to false' -e 'end tell' -e 'tell application \"Finder\" to set collapsed of windows to true'"
    print command
    run_command(command)

def max_vol():
    command = "osascript -e 'set volume output volume 100'"
    run_command(command)

def open_chrome(url):
    max_vol()
    command = "open '"+url+"'"
    run_command(command)


def open_chrome_rand_url():
    urls = [
        "https://www.projectsmart.co.uk/top-10-qualities-project-manager.php",
        "https://www.youtube.com/watch?v=mIBccpqUcgY&list=PLYhRb-ZJrxrycBd4DhTXkzPRtRPMUnpFv",
        "https://www.youtube.com/watch?v=sc0mi0Ei1CQ",
        "http://stackoverflow.com/questions/84556/whats-your-favorite-programmer-cartoon/84629#84629",
        "http://dilbert.com/strip/2010-07-01",
        "https://www.google.co.il/webhp?sourceid=chrome-instant&ion=1&espv=2&ie=UTF-8#q=how+to+become+a+good+product+manager",
        "http://sd.keepcalm-o-matic.co.uk/i/keep-calm-and-stop-thinking-of-cigarettes.png",
        "https://www.youtube.com/watch?v=zIQvECPmMiw",
    ]
    url = random.choice(urls)
    open_chrome(url)

def open_app():
    apps = ["/Applications/iTunes.app",
           "/Applications/Photos.app",
            "dict://piano",
           ]
    app = random.choice(apps)
    run_command("open "+app)

def log_to_file():
    run_command("echo `date` >> /tmp/a")

while True:
    time.sleep(sleep_time)

    run_command("curl --HEAD https://someserver/url?troll")
    if time.localtime().tm_hour <= end_hour and time.localtime().tm_hour >= start_hour:
        options = [mini_windows,open_chrome_rand_url,open_app]
        random.choice(options)()
        #log_to_file()

