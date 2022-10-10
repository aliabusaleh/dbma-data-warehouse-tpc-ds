
#!/usr/bin/env bash

# File for collecting result of 
#
#
# USAGE: ./mysql_result_summary <SCALE>
# EXAMPLE: ./mysql_result_summary 1

DB_RESULTS_DIR=/home/aliabusaleh/PycharmProjects/DataWarehouse/query_results/${1}/
CSV_NAME=query_time_scale_factor_${1}.csv
SUMMARY_DIR=`pwd`

rm -rf $SUMMARY_DIR/$CSV_NAME

for f in `ls $DB_RESULTS_DIR/*.log`
    # Mac OS
    #do TIME=`cat $f | awk '{print $1}'`
    #echo "`basename ${f%.*}`,$TIME" >> $SUMMARY_DIR/$CSV_NAME

    # ubuntu OS
    do TIME=`head -1 $f |  awk '{print $3}' | awk '{sub(/\(.*/, "", $(NF-1)); print $1}'`
    echo "`basename ${f%.*>}`,$TIME" >> $SUMMARY_DIR/$CSV_NAME
done
