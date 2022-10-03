#!/usr/bin/env bash
# This file exeucte tpcds queries in mysql.#
#
# Multiple cores can be used by setting CPUS flag
#
# USAGE: ./mysql_execute_queries.sh <SCALE> <CPUS>
# EXAMPLE: ./mysql_execute_queries.sh 1 2

SCALE=$1
QUERY_DIR="/Users/rizwan/Downloads/ULB/dw/project/tpcds_toolkit/queries"
OUTPUT_DIR="/Users/rizwan/Downloads/ULB/dw/project/tpcds_toolkit/query_results/${SCALE}"
SCRIPT_DIR=/Users/rizwan/Downloads/ULB/dw/project/tpcds_toolkit/scripts
DB_NAME="tpcds_${SCALE}"

mkdir -p $OUTPUT_DIR

CORES=$2

if [ -z $CORES ]; then 
    CORES=1;
fi

set -e

ls $QUERY_DIR/query*.sql | xargs -P $CORES -n 1 $SCRIPT_DIR/mysql_execute_query.sh $SCALE $OUTPUT_DIR $DB_NAME