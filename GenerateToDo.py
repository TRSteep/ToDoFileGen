### Library ###
from calendar import monthrange
from pathlib import Path

### Data ###
year = 2013
pathfolder = "K:/Projects/TODO/"

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
    pathfile = pathfolder+'TODO_'+str(year)+'.'+monthtext+'.01.txt'
    #print(pathfile)
    with open(pathfile,"w") as file:
        ### Days in mounth ###
        days = 0
        while days!=num_days:
            days=days+1;

            #print("days: %d" % (days))
            file.write("{-------------------------------[   %d.%s.%d   ]-------------------------------\n" % (year, monthtext, days))
            for x in range(3):
                file.write("{---\n")
                file.write("\t\n")
                file.write("---}\n")
            file.write("--------------------------------------------------------------------------------}\n")
            
            ### File close ###
        file.close()