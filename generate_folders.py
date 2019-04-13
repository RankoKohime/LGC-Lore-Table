#!/usr/bin/python3
import datetime
import dateutil
from dateutil import rrule
import os
import sys
#from dateutil.parser import *

# Set the working year, given as the singluar argument when called.
try:
    MAKE_YEAR = int(sys.argv[1])
except IndexError:
    print('I think you forgot the year there Brad.')
    sys.exit(1)

# Start date (January 1st of MAKE_YEAR)
CUR = datetime.date(year=MAKE_YEAR, month=1, day=1)

# End Date (December 31st of next year)
END = datetime.date(year=MAKE_YEAR, month=12, day=31)

# Checks the difference between two dates for calculating the episode number
# https://stackoverflow.com/questions/8419564/difference-between-two-dates-in-python

# Arguments are
# d1 = first episode date
# d2 = current episode date
def episode_num(d1, d2):
    weeks = rrule.rrule(rrule.WEEKLY, dtstart=d1, until=d2)
    return weeks.count()

# Creates the seasonal directory if it doesn't exist,
# then touches all .md files for that season.
def touch_file(show, make_year, season, ep_date, ep_num):
    SEASONAL_DIRECTORY = show + '/' + str(make_year) + ' - Season ' + str(season)
    EPISODE_DATE = datetime.datetime.strptime(str(CUR), '%Y-%m-%d').strftime('%Y%m%d')
    EPISODE_NAME = str(EPISODE_DATE) + "-" + str(ep_num).zfill(4)
  # Arguments are
  # 1. Which show
  # 2. Year being generated
  # 3. Which season for the individual show
  # 4. Episode date
  # 5. Episode number

  # Create the seasonal directory
    if not os.path.isdir(SEASONAL_DIRECTORY):
        print("Created the directory " + SEASONAL_DIRECTORY)
        os.makedirs(SEASONAL_DIRECTORY)

  # Create the episode directory
    if not os.path.isdir(SEASONAL_DIRECTORY + "/" + EPISODE_NAME):
        print("Created the directory " + SEASONAL_DIRECTORY + "/" + EPISODE_NAME)
        os.makedirs(SEASONAL_DIRECTORY + "/" + EPISODE_NAME)

# Checking sanity manually at runtime
if not input("Are you sure you want to run?  Will be working on calendar year " + str(MAKE_YEAR) + " (y/n): ").lower().strip()[:1] == "y": sys.exit(1)

# Loop through every day in the year, and create directories
# and files as appropriate, stopping at the end of the year (but not the day before)
while CUR <= END:
    if CUR.weekday() == 2:
        # Test if $cur is a Wednesday, then generate LWDW template
        LWDW_START = datetime.datetime(2016, 2, 17)  # Adjusted from 2016, 2, 10 because math.  ¯\_(ツ)_/¯
        SEASON = MAKE_YEAR - 2015
        EP_NUM = episode_num(LWDW_START, CUR)
        touch_file("LWDW", MAKE_YEAR, SEASON, CUR, EP_NUM)
    # Test if $cur is a Saturday, then generate LGCW template
    elif CUR.weekday() == 5:
        LGCW_START = datetime.datetime(2012, 8, 25)  # Adjusted from 2012, 8, 18 because math.  ¯\_(ツ)_/¯
        SEASON = MAKE_YEAR - 2011
        EP_NUM = episode_num(LGCW_START, CUR)
        touch_file("LGCW", MAKE_YEAR, SEASON, CUR, EP_NUM)
    CUR = CUR + datetime.timedelta(days=1)
