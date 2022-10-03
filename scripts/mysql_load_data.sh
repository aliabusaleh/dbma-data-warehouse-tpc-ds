#!/usr/bin/env bash
# For loading the data in to tpcds database.
# This file assumes that the file and table have same names and the schema is already created.
# 
# USAGE: ./mysql-load-data <DB_NAME> <DAT_FILE>
# ./mysql_load_data tpcds data/1/call_center.dat

DB_NAME=$1
file=$2

table=`basename $file .dat | sed -e 's/_[0-9]_[0-9]//'`
mysql -uroot -pTemp/123 -D$DB_NAME -e "TRUNCATE $table"
mysql --local_infile=1 --default-character-set=latin1 -uroot -pTemp/123 -D$DB_NAME -e "LOAD DATA LOCAL INFILE '$file' INTO TABLE $table FIELDS TERMINATED BY '|' LINES TERMINATED BY '\n'"