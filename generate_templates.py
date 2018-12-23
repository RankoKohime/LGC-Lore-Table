#!/usr/bin/python3
import sys
import os
import datetime
#import dateutil
from dateutil import rrule


# Set the working year, which should be next year.
年を作る = datetime.date.today().year + 1

# Start date (January 1st of 年を作る)
現在 = datetime.date(year=年を作る, month=1, day=1)

# End Date (December 31st of next year)
終わり = datetime.date(year=年を作る, month=12, day=31)

# Checks the difference between two dates for calculating the episode number
# https://stackoverflow.com/questions/8419564/difference-between-two-dates-in-python

def エピソード番号(発生エピソード, 現在のエピソード):
    weeks = rrule.rrule(rrule.WEEKLY, dtstart=発生エピソード, until=現在のエピソード)
    return weeks.count()

# Creates the seasonal directory if it doesn't exist,
# then touches all .md files for that season.

def タッチファイル(見せる, make_year, シーズン, ep_date, ep_num):
    季節別ディレクトリ = 見せる + '/' + str(make_year) + ' - Season ' + str(シーズン)
    # Arguments are
    # 1. Which show
    # 2. Year being generated
    # 3. Which season for the individual show
    # 4. Episode date
    # 5. Episode number

  # Create the directory
    if not os.path.isdir(季節別ディレクトリ):
        print("Created the directory " + 季節別ディレクトリ)
        os.makedirs(季節別ディレクトリ)

    # Touch the file in it's naughty place
    エピソード日 = datetime.datetime.strptime(str(現在), '%Y-%m-%d').strftime('%Y%m%d')
    エピソード名 = str(エピソード日) + "-" + str(ep_num).zfill(4) + ".md"
    print("Created the file " + 季節別ディレクトリ + "/" + エピソード名)
    f = open(季節別ディレクトリ + "/" + エピソード名, "w")
    if 見せる == "LGCW":
        f.write(str(ep_num) + '. \n     * ' + str(ep_date) + '\n        * [Showzen]()\n        * [Patreon]()\n        * [UNCUT Patreon]()\n     * <span style="color:red">LGC Weekly:</span> \n')
    elif 見せる == "LWDW":
        f.write(str(ep_num) + '. \n     * ' + str(ep_date) + '\n        * [Patreon]()\n        * [UNCUT Patreon]()\n')

# Checking sanity manually at runtime
if not input("Are you sure you want to run?  Will be working on calendar year " + str(年を作る) + " (y/n): ").lower().strip()[:1] == "y": sys.exit(1)

# Loop through every day in the year, and create directories
# and files as appropriate, stopping at the end of the year
# (but not the day before, in case a show falls on New Years Eve)
while 現在 <= 終わり:
    # Test if $cur is a Wednesday, then generate LWDW template
    if 現在.weekday() == 2:
        # Adjusted from 2016, 2, 10 because math.  ¯\_(ツ)_/¯
        LWDW_開始 = datetime.datetime(2016, 2, 17)
        季節 = 年を作る - 2015
        数 = エピソード番号(LWDW_開始, 現在)
        タッチファイル("LWDW", 年を作る, 季節, 現在, 数)
    # Test if $cur is a Saturday, then generate LGCW template
    elif 現在.weekday() == 5:
        # Adjusted from 2012, 8, 18 because math.  ¯\_(ツ)_/¯
        LGCW_開始 = datetime.datetime(2012, 8, 25)
        季節 = 年を作る - 2011
        数 = エピソード番号(LGCW_開始, 現在)
        タッチファイル("LGCW", 年を作る, 季節, 現在, 数)
    現在 = 現在 + datetime.timedelta(days=1)
