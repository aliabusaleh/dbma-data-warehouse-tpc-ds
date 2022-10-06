
#!/usr/bin/env bash
# For generating the TPCDS Data
# This script will be run to generate mysql compatible data
#
# USAGE: ./mysql_generate_data <SCALE>
# ./mysql_generate_data 1

SCALE=$1
DATA_DIR="/home/aliabusaleh/Desktop/ulb/tpcds-kit/data/${SCALE}"
TOOLS_DIR=/home/aliabusaleh/Desktop/ulb/tpcds-kit/tools

mkdir -p $DATA_DIR

pushd $TOOLS_DIR
./dsdgen -SCALE $SCALE -DIR $DATA_DIR -VERBOSE Y
popd

# For Mac OS
# LC_CTYPE=C && sed -i '' -e 's_^|_\\N|_g' -e 's_||_|\\N|_g' -e 's_||_|\\N|_g' $DATA_DIR/*.dat

# For Linux
LC_CTYPE=C && sed -i -e 's_^|_\\N|_g' -e 's_||_|\\N|_g' -e 's_||_|\\N|_g' $DATA_DIR/*.dat