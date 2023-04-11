from datetime import datetime
year = '2023'
month = '04'
days = '01'

date_text = (year + month + days)
date_format = "%Y%m%d"
date_data = datetime.strptime(date_text, date_format)
print(date_data)
weekday = date_data.weekday()
print(weekday)
if weekday >= 5:
    print("WeekEnd")