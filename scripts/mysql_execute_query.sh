#!/usr/bin/env sh
# script to run a query in mysql tpcds database.
# This file will output 3 files for query
#
# 1. Log file (time) 2. Error file 3. Result File
#
# USAGE: ./mysql_execute_query.sh <OUTPUT_DIR> <DB_NAME> <QUERY_FILE>
# EXAMPLE ./mysql_execute_query query_results/ tpcds query1.sql

/usr/bin/time -o "$1/`basename ${3%.*}`.log" mysql -uroot -pTemp/123 $2 < $3 > "$1/`basename ${3%.*}`.res" 2> "$1/`basename ${3%.*}`.err"