### TODO Generator ###
#
#   Generate TODO text files each month,  
#   in file each day generating Tasks (on weekend 1 task)
#
### Library ###
from calendar import monthrange
from datetime import datetime
from pathlib import Path

### Changed Data ###
year = 2023
pathfolder = "C:/Media/dev/python/ToDoFileGen/TODO/"

## Data Operation ##
yeartext = str(year)
date_format = "%Y%m%d"

### Mounth ###
month = 0
while month!=12:
    month=month+1;
    num_days = monthrange(year, month)[1] # num_days = 28
    #print("month: %d, num_days: %d" % (month, num_days))
    
    ##Month in text
    if month < 10:
        monthtext = '0'+str(month)
    else:
        monthtext = str(month)
    
    ### Create mouth file ###
    # Create file TODO_Year.Date.01_.txt
    pathfile = pathfolder+'TODO_'+yeartext+'.'+monthtext+'.01.txt'
    #print(pathfile)
    with open(pathfile,"w") as file:
        ### Days in mounth ###
        days = 0
        while days!=num_days:
            days=days+1;
            if days < 10:
                daytext = '0'+str(days)
            else:
                daytext = str(days)

            # Find Day of week
            date_text = (yeartext + monthtext + daytext)
            #print(date_text)
            date_data = datetime.strptime(date_text, date_format)
            weekday = date_data.weekday()

            #print("days: %d" % (days))
            #print(weekday)
            file.write("{-------------------------------[   %s.%s.%s   ]-------------------------------\n" % (yeartext, monthtext, daytext))
            if weekday < 5:
                for x in range(5):
                    file.write("{\t\n")
                    file.write("\t\n")
                    file.write("\t\n")
                    file.write("-}\n")
                    #print("WorkDay")
            else:
                for x in range(1):
                    file.write("{\t\n")
                    file.write("\t\n")
                    file.write("-}\n")
                    #print("WeekEnd")
            file.write("--------------------------------------------------------------------------------}\n")
            
            ### File close ###
        file.close()