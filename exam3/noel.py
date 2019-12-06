#!/usr/bin/python3
import sys
import calendar
from datetime import datetime
def show_noel(allArg):
    if len(allArg) > 1:
        date_time_str = allArg[1]
        theDate = datetime.strptime(date_time_str, '%Y-%m-%d')
    else:
        theDate = datetime.now()
    yearForChristmas = datetime.now().year

    # Définit si noël aura lieu cette année ou l'année prochaine (Si on est le 26 Décembre par exemple)

    if theDate.strftime('%Y-%m-%d') > str(datetime.now().year)+"-12-25":
        yearForChristmas = datetime.now().year+1
    dateToNextChristmas = datetime.strptime(str(yearForChristmas)+"-12-25", "%Y-%m-%d")
    daysBfChristmas = str(abs((dateToNextChristmas - theDate).days))+" days before christmas\n"
    c = calendar.TextCalendar(calendar.MONDAY)
    firstCalendar = c.formatmonth(theDate.year, theDate.month, 5, 1)
    firstCalendar = firstCalendar.replace(str(theDate.day), "("+str(theDate.day)+")", 1)
    c = calendar.TextCalendar(calendar.MONDAY)
    secondCalendar = c.formatmonth(yearForChristmas, 12, 5, 1)
    secondCalendar = secondCalendar.replace(" 25 ", "[25]", 1)
    sapin = """
        x
       xxx
      xxxxx
     xxxxxxx
    xxxxxxxxx
   xxxxxxxxxxx
  xxxxxxxxxxxxx
 xxxxxxxxxxxxxxx
       xxx
       xxx
       xxx
       xxx
        """
    if theDate.strftime('%Y-%m-%d') == str(theDate.year)+"-12-25":
        return sapin
    else:
        return daysBfChristmas+firstCalendar+secondCalendar
if __name__ == "__main__":
    print(show_noel(sys.argv))
