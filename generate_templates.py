#!/usr/bin/python3
from datetime import date

# Get next year
MAKE_YEAR = str(date.today().year + 1)

# Start date
CUR = MAKE_YEAR + "0101"

# End Date
END = MAKE_YEAR + "1231"

print("Are you sure you want to run?  Will be working on calendar year " + MAKE_YEAR)

# Loop through every day in the year, and create directories
# and files as appropriate, stopping at the end of the year


#LGCW = All dates/episode numbers of LGCW

#LWDW = All dates/episode numbers of LWDW

#for episode in LGCW:
#------------------------------------------
# All code below this point is shell scrap!
#------------------------------------------
#read -n 1
#if [[ $REPLY =~ ^[Yy]$ ]]
#  then
#    while [ $cur -le $end ]
#      do
#        if [ $(date -d $cur +%w) == "3" ]
#          then
#            echo -e "LWDW code here, $cur, `date -d $cur`"
#            touch_lwdw $cur $lwdw_episode
#          elif [ $(date -d $cur +%w) == "6" ]
#            echo -e "LGCW code here, $cur, `date -d $cur`"
#            touch_lgcw $cur $lgcw_episode
#          fi
#        fi
#        cur=`date -d "$cur+1days" +%Y%m%d`
#    done
#  else
#    echo -e "Cancelling"
#    exit 1
#fi

# Creates the seasonal directory if it doesn't exist,
# then touches all .md files for that season.
#touch_file()
#{
  # Create the directory
#  seasonal_directory=$1/$2
#  if [ -d $seasonal_directory ]; then
#    echo -e "We are creating the directory $seasonal_directory"
    #mkdir -p $seasonal_directory
#  fi

  # Touch the file in it's naughty place
#  episode_date=$cur
#  episode_date_hr=`date -d "$episode_date" +%Y-%m-%d`
#  episode_number=1  #Placeholder
#  episode_name=$episode_date-$episode_number.md
#  echo -e "We are creating the file $seasonal_directory/$episode_name"
  #touch $episode_name

#}
