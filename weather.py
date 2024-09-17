import requests
from bs4 import BeautifulSoup
from win10toast import ToastNotifier

notifier = ToastNotifier()

def getdata(url):
    r = requests.get(url)
    return r.text

def get_weather():
    htmldata = getdata("https://weather.com/en-IN/weather/today/l/25.59,85.14?par=google&temp=c/")

    soup = BeautifulSoup(htmldata, 'html.parser')

    current_temp = soup.find_all("span", class_="CurrentConditions--tempValue--MHmYY")


    temp = (str(current_temp[0]))
    temp = temp.replace("<span class=\"CurrentConditions--tempValue--MHmYY\" data-testid=\"TemperatureValue\" dir=\"ltr\">", " ")
    temp = temp.replace("<span class=\"CurrentConditions--degreeSymbol--4RS_X\">°</span><span></span></span>", " ")

    result = "current_temp is" + temp + "in patna bihar"
    notifier.show_toast("live Weather update", result, duration=5)