
#!/usr/bin/env bash
# This file creates mysql database schema as per scale factor and loads data to mysql
#
# USAGE: ./mysql_db_load.sh <SCALE> <CPUS>
# EXAMPLE: ./mysql-db-load.sh 1 2

SCALE=$1
SCHEMA_DIR=/Users/rizwan/Downloads/ULB/dw/project/tpcds_toolkit/tools
DATA_DIR="/Users/rizwan/Downloads/ULB/dw/project/tpcds_toolkit/data/${SCALE}"
SCRIPT_DIR=/Users/rizwan/Downloads/ULB/dw/project/tpcds_toolkit/scripts
DB_NAME="tpcds_${SCALE}"

CORES=$1

if [ -z $CORES ]; then 
    CORES=1;
fi

# exit on error
set -e

mysql -uroot -pTemp/123 -e "drop database if exists $DB_NAME;"
mysql -uroot -pTemp/123 -e "create database $DB_NAME;"
mysql -uroot -pTemp/123 -D$DB_NAME < $SCHEMA_DIR/tpcds.sql

ls $DATA_DIR/*.dat | xargs -P $CORES -n 1 $SCRIPT_DIR/mysql_load_data.sh $DB_NAME

rm -rf $DATA_DIR