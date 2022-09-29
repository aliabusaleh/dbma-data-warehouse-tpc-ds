import os
import argparse

# Create the parser
parser = argparse.ArgumentParser()

# Add an argument
parser.add_argument('--dsqgen_tool', type=str, required=True)
parser.add_argument('--output_dir', type=str, required=False)
parser.add_argument('--scale', type=int, nargs='+', required=True)

# Parse the argument
args = parser.parse_args()

DSQGEN_TAG = "./dsqgen"
SPACE_TAG = " "
FLAG_TAG = "-"
DIR_TAG = "/"
OUTPUT_DIR_TAG = "output_dir"
OUTPUT_DIR = "../dsqgen_out/"
QUALIFY_TAG = "qualify"
QUALIFY = "Y"
SCALE_TAG = "scale"
SCALE = [1,10,25,50]
DIALECT_TAG = "dialect"
DIALECT = "mysql"
DIRECTORY_TAG = "directory"
DIRECTORY = "../query_templates/"
TEMPLATE_TAG = "template"
TEMPLATE = "query{}.tpl"

if not os.path.exists(args.dsqgen_tool):
    raise Exception("Empty path, you should provide the full file path and name")
else:
    os.chdir(args.dsqgen_tool)
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

for scale in args.scale:
    os.makedirs(OUTPUT_DIR + str(scale))
    temp_out_dir = OUTPUT_DIR + str(scale)
    for query in range(1,100):


        bash_script = DSQGEN_TAG + SPACE_TAG + FLAG_TAG + OUTPUT_DIR_TAG + SPACE_TAG + temp_out_dir + SPACE_TAG \
                      + FLAG_TAG + SCALE_TAG + SPACE_TAG + str(scale) + SPACE_TAG + FLAG_TAG + DIALECT_TAG \
                      + SPACE_TAG + DIALECT + SPACE_TAG + FLAG_TAG + DIRECTORY_TAG + SPACE_TAG + DIRECTORY \
                      + SPACE_TAG + FLAG_TAG + TEMPLATE_TAG + SPACE_TAG + TEMPLATE.format(query)
        os.system(bash_script)
        os.rename(temp_out_dir+"/query_0.sql", temp_out_dir+"/query{}.sql".format(query))


#./dsqgen -output_dir ../dsqgen_out/ -scale 1 -qualify Y -dialect mysql -directory ../query_templates -template query1.sql