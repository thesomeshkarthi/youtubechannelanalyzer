from flask import Flask, render_template, request
from datetime import datetime
from dateutil import relativedelta
import urllib.request
import json
import os

#I have protected my API Key by using a local environment variable
key = os.environ['API_KEY']

app = Flask(__name__)

@app.route('/')
def searchscreen():
    return render_template('searchscreen.html')

@app.route('/', methods= ['POST'])
def analyzeUsername():
    username = request.form['username']
    if (len(username) == 24) and (username[:2] == "UC"):
        channelurl = "https://www.googleapis.com/youtube/v3/channels?part=snippet%2CcontentDetails%2Cstatistics&id=" + username + "&key=" + key
        channeldata = urllib.request.urlopen(channelurl).read()
        channelname = json.loads(channeldata)["items"][0]["snippet"]["title"]
        channelsubs = json.loads(channeldata)["items"][0]["statistics"]["subscriberCount"]
        channelsubs = int(channelsubs)
        channelviews = json.loads(channeldata)["items"][0]["statistics"]["viewCount"]
        channelviews = int(channelviews)
        channelvideos = json.loads(channeldata)["items"][0]["statistics"]["videoCount"]
        channelvideos = int(channelvideos)
        channelpic = json.loads(channeldata)["items"][0]["snippet"]["thumbnails"]["medium"]["url"]
        channelbio = json.loads(channeldata)["items"][0]["snippet"]["description"]
        channeldate = json.loads(channeldata)["items"][0]["snippet"]["publishedAt"]
        channelday = channeldate[8:10]
        channelyear = channeldate[:4]
        channelmonth = channeldate[5:7]
        channelborn = datetime(int(channelyear), int(channelmonth), int(channelday))
        if channelmonth == "01":
            channelmonth = "January"
        elif channelmonth == "02":
            channelmonth = "February"
        elif channelmonth == "03":
            channelmonth = "March"
        elif channelmonth == "04":
            channelmonth = "April"
        elif channelmonth == "05":
            channelmonth = "May"
        elif channelmonth == "06":
            channelmonth = "June"
        elif channelmonth == "07":
            channelmonth = "July"
        elif channelmonth == "08":
            channelmonth = "August"
        elif channelmonth == "09":
            channelmonth = "September"
        elif channelmonth == "10":
            channelmonth = "October"
        elif channelmonth == "11":
            channelmonth = "November"
        else:
            channelmonth = "December"
        channeldate = channelmonth + " " + channelday + ", " + channelyear
        channeltime = json.loads(channeldata)["items"][0]["snippet"]["publishedAt"]
        channelhour = int(channeltime[11:13])
        if channelhour > 12:
            channelhour = channelhour - 12
            channelsetting = "PM"
        elif channelhour == 00 or channelhour == 24:
            channelhour = 12
            channelsetting = "AM"
        else:
            channelhour = channelhour
            channelsetting = "AM"
        channelhour = str(channelhour)
        channelminute = channeltime[14:16]
        channeltime = channelhour + ":" + channelminute + " " + channelsetting
        today = datetime.now()
        channelage = relativedelta.relativedelta(today, channelborn)
        channelageyears = channelage.years
        channelagemonths = channelage.months
        channelagedays = channelage.days
        if channelvideos == 0 or channelviews == 0:
            channelaverageviews = 0
        else:
            channelaverageviews = round(channelviews / channelvideos)
        channelperfectratio = (channelsubs * 0.14)
        if channelvideos == 0 or channelviews == 0 or channelaverageviews == 0 or channelperfectratio == 0:
            channelgrade = "D"
            channelgradecolor = "#8B0000"
        else:
            channelgrade = (channelaverageviews / channelperfectratio)
            if channelgrade >= 1:
                channelgrade = "A"
                channelgradecolor = "#7CFC00"
            elif channelgrade >= 0.75:
                channelgrade = "B"
                channelgradecolor = "#FFFF00"
            elif channelgrade >= 0.5:
                channelgrade = "C"
                channelgradecolor = "#FFA500"
            else:
                channelgrade = "D"
                channelgradecolor = "#8B0000"
    else:
        channelurl = "https://www.googleapis.com/youtube/v3/channels?part=snippet%2CcontentDetails%2Cstatistics&forUsername=" + username + "&key=" + key
        channeldata = urllib.request.urlopen(channelurl).read()
        channelname = json.loads(channeldata)["items"][0]["snippet"]["title"]
        channelsubs = json.loads(channeldata)["items"][0]["statistics"]["subscriberCount"]
        channelsubs = int(channelsubs)
        channelviews = json.loads(channeldata)["items"][0]["statistics"]["viewCount"]
        channelviews = int(channelviews)
        channelvideos = json.loads(channeldata)["items"][0]["statistics"]["videoCount"]
        channelvideos = int(channelvideos)
        channelpic = json.loads(channeldata)["items"][0]["snippet"]["thumbnails"]["medium"]["url"]
        channelbio = json.loads(channeldata)["items"][0]["snippet"]["description"]
        channeldate = json.loads(channeldata)["items"][0]["snippet"]["publishedAt"]
        channelday = channeldate[8:10]
        channelyear = channeldate[:4]
        channelmonth = channeldate[5:7]
        channelborn = datetime(int(channelyear), int(channelmonth), int(channelday))
        if channelmonth == "01":
            channelmonth = "January"
        elif channelmonth == "02":
            channelmonth = "February"
        elif channelmonth == "03":
            channelmonth = "March"
        elif channelmonth == "04":
            channelmonth = "April"
        elif channelmonth == "05":
            channelmonth = "May"
        elif channelmonth == "06":
            channelmonth = "June"
        elif channelmonth == "07":
            channelmonth = "July"
        elif channelmonth == "08":
            channelmonth = "August"
        elif channelmonth == "09":
            channelmonth = "September"
        elif channelmonth == "10":
            channelmonth = "October"
        elif channelmonth == "11":
            channelmonth = "November"
        else:
            channelmonth = "December"
        channeldate = channelmonth + " " + channelday + ", " + channelyear
        channeltime = json.loads(channeldata)["items"][0]["snippet"]["publishedAt"]
        channelhour = int(channeltime[11:13])
        if channelhour > 12:
            channelhour = channelhour - 12
            channelsetting = "PM"
        elif channelhour == 00 or channelhour == 24:
            channelhour = 12
            channelsetting = "AM"
        else:
            channelhour = channelhour
            channelsetting = "AM"
        channelhour = str(channelhour)
        channelminute = channeltime[14:16]
        channeltime = channelhour + ":" + channelminute + " " + channelsetting
        today = datetime.now()
        channelage = relativedelta.relativedelta(today, channelborn)
        channelageyears = channelage.years
        channelagemonths = channelage.months
        channelagedays = channelage.days
        if channelvideos == 0 or channelviews == 0:
            channelaverageviews = 0
        else:
            channelaverageviews = round(channelviews / channelvideos)
        channelperfectratio = (channelsubs * 0.14)
        if channelvideos == 0 or channelviews == 0 or channelaverageviews == 0 or channelperfectratio == 0:
            channelgrade = "D"
            channelgradecolor = "#8B0000"
        else:
            channelgrade = (channelaverageviews / channelperfectratio)
            if channelgrade >= 1:
                channelgrade = "A"
                channelgradecolor = "#7CFC00"
            elif channelgrade >= 0.75:
                channelgrade = "B"
                channelgradecolor = "#FFFF00"
            elif channelgrade >= 0.5:
                channelgrade = "C"
                channelgradecolor = "#FFA500"
            else:
                channelgrade = "D"
                channelgradecolor = "#8B0000"
    return render_template('outputscreen.html', cn = channelname, cs = ("{:,}".format(channelsubs)), cvw = ("{:,}".format(channelviews)), cvd = ("{:,}".format(channelvideos)), cp = channelpic, cb = channelbio, cd = channeldate, ct = channeltime, cay = channelageyears, cam = channelagemonths, cad = channelagedays, cav = ("{:,}".format(channelaverageviews)), cg = channelgrade, cgc = channelgradecolor)


if __name__ == '__main__':
    app.run(debug = True)
