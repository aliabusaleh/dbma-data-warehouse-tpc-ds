# This is a sample Python script.
import os
import threading
from time import sleep

from utils.file_modifications import handle_null_values
from utils.sql_scripts import *
from mysql_class import MySQl


def pre_processing(db_name, db_schema_path, db_schema_path_file, data_root_path):
    # 1- drop db if exist
    drop_db_sql = construct_drop_db(db_name=DB_NAME)

    # 2- create new DB
    create_db_sql = construct_create_db(db_name=DB_NAME)

    # 3- create schema for db
    create_schema_sql = construct_create_schema(db_schema_file_path=DB_SCHEMA_PATH, file_name=DB_SCHEMA_FILE_NAME)

    # 4- load the files names
    data_file_list = os.listdir(DATA_ROOT_PATH)

    # 5-  create load sql statements
    load_data_sqls = []
    for table_data in data_file_list:
        load_data_sqls.append(load_data_into_table(data_parent_file_path=DATA_ROOT_PATH, file_name=table_data))

    return drop_db_sql, create_db_sql, create_schema_sql, data_file_list, load_data_sqls

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # DB name
    DB_NAME = 'tpcds'
    # create tables vars
    DB_SCHEMA_PATH = os.environ['DB_SCHEMA_PATH']
    DB_SCHEMA_FILE_NAME = os.environ['DB_SCHEMA_FILE_NAME']
    # load the data vars
    DATA_ROOT_PATH = os.environ['DATA_ROOT_PATH']

    # pre processing
    drop_db_sql, create_db_sql, \
    create_schema_sql, data_file_list, \
    load_data_sqls = pre_processing(db_name=DB_NAME,
                                    db_schema_path_file=DB_SCHEMA_FILE_NAME,
                                    db_schema_path=DB_SCHEMA_PATH,
                                    data_root_path=DATA_ROOT_PATH)

    # start processing

    # - fix generated data files
    for table_data in data_file_list:
        handle_null_values(DATA_ROOT_PATH + table_data)


    # start executing
    sql_instance = MySQl()
    sql_instance.execute_statement(drop_db_sql)
    sql_instance.execute_statement(create_db_sql)
    sql_instance.execute_statement(create_schema_sql, multi=False)
    sleep(3)
    for data_sql in load_data_sqls:
        sql_instance.execute_statement(data_sql, multi=False)
    print("finish")