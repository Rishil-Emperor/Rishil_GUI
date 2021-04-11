import datetime
import pytz
import json

with open('time_zones.json', 'r') as f:
    time_zones = json.load(f)

# This is where the GUI (PyQt5) code will be.

today_date = datetime.date.today()
today_year = today_date.year
month = today_date.month
today_day = today_date.day
months = {
    "1": "January",
    "2": "February",
    "3": "March",
    "4": "April",
    "5": "May",
    "6": "June",
    "7": "July",
    "8": "August",
    "9": "September",
    "10": "October",
    "11": "November",
    "12": "December"
}
today_month = months[str(month)]
print([today_year, today_month, today_day])