#!/bin/bash
#set -Eeuxo pipefail

# Get the next year
make_year=`date -d "+1year" +%Y`
# Start date
cur=${make_year}0101
# End date
end=${make_year}1231

# Checks the difference between two dates for calculating the episode number
# https://unix.stackexchange.com/a/24636
episode_num()
(
    d2=$(date -d "$1" +%s)
    d1=$(date -d "$2" +%s)
    echo $(( (d1 - d2) / 86400 / 7 ))
)

# Creates the seasonal directory if it doesn't exist,
# then touches all .md files for that season.
touch_file()
(
  # Arguments are
  # 1. Which show
  # 2. Year being generated
  # 3. Which season for the individual show
  # 4. Episode date
  # 5. Episode number

  # Create the directory
  seasonal_directory="$1/$2 - Season $3"
  echo -e $seasonal_directory
  if [[ ! -d "$seasonal_directory" ]]; then
    echo -e "Created the directory $seasonal_directory"
    mkdir -p "$seasonal_directory"
  fi

  # Touch the file in it's naughty place
  episode_date=`date -d "$4" +%Y%m%d`
  episode_date_hr=`date -d $episode_date +%Y-%m-%d`
  episode_name=$episode_date-$5.md
  echo -e "Created the file $seasonal_directory/$episode_name"
  #touch $seasonal_directory/$episode_name
  echo -e "$5. \n     * $episode_date_hr\n        * [Showzen]()\n        * [Patreon]()\n        * [UNCUT Patreon]()\n     * <span style="color:red">LGC Weekly:</span> " >> "$seasonal_directory/$episode_name"
)

# Loop through every day in the year, and create directories
# and files as appropriate, stopping at the end of the year

echo -e "Are you sure you want to run?  Will be working on calendar year $make_year"
read -n 1
if [[ $REPLY =~ ^[Yy]$ ]]
  then
    # Loop until we reach the end of the year
    while [ $cur -le $end ]
      do
        # Test if $cur is a Wednesday, then generate LWDW template
        if [ $(date -d $cur +%w) == 3 ]
          then
            lwdw_episode=$( episode_num 20160210 $cur )
            season=$(($make_year-2015))
            touch_file LWDW $make_year $season $cur $lwdw_episode
        # Test if $cur is a Saturday, then generate LGCW template
        elif [ $(date -d $cur +%w) == 6 ]
          then
            lgcw_episode=$( episode_num 20120818 $cur )
            season=$(($make_year-2011))
            touch_file LGCW $make_year $season $cur $lgcw_episode
        fi
        cur=`date -d "$cur+1days" +%Y%m%d`
    done
  else
    echo -e "Cancelling"
    exit 1
fi
