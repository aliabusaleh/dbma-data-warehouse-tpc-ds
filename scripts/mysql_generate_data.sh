#!/usr/bin/env bash
# For generating the TPCDS Data
# This script will be run to generate mysql compatible data
# 
# USAGE: ./mysql_generate_data <SCALE>
# ./mysql_generate_data 1

SCALE=$1
DATA_DIR="/Users/rizwan/Downloads/ULB/dw/project/tpcds_toolkit/data/${SCALE}"
TOOLS_DIR=/Users/rizwan/Downloads/ULB/dw/project/tpcds_toolkit/tools

mkdir -p $DATA_DIR

pushd $TOOLS_DIR
./dsdgen -SCALE $SCALE -DIR $DATA_DIR -VERBOSE Y -PARALLEL 4 -CHILD 1
./dsdgen -SCALE $SCALE -DIR $DATA_DIR -VERBOSE Y -PARALLEL 4 -CHILD 2
./dsdgen -SCALE $SCALE -DIR $DATA_DIR -VERBOSE Y -PARALLEL 4 -CHILD 3
./dsdgen -SCALE $SCALE -DIR $DATA_DIR -VERBOSE Y -PARALLEL 4 -CHILD 4
popd

LANG=C && sed -i '' -e 's/^|/\N|/' -e 's/||/|\N|/g' -e 's/||/|\N|/g' -e 's/|$/|/' $DATA_DIR/*.dat