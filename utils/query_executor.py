import os
import tqdm
import argparse
from mysql_class import MySQl

sql_instance = MySQl()

# Create the parser
parser = argparse.ArgumentParser()

# Add an argument
parser.add_argument('--query_path', type=str, required=True)
parser.add_argument('--scale', type=int, nargs='+', required=True)

# Parse the argument
args = parser.parse_args()

for scale in args.scale:
    query_path = args.query_path + str(scale) + "/"
    files = sorted(os.listdir(query_path))
    for file in files:
        fd = open(query_path+file,"r")
        sql = fd.read()
        fd.close()
        print(query_path + file + " " + str(sql_instance.execute_query(sql,'tpcds')))
