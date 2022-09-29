from os.path import exists

from utils.validator import check_file_existence


def construct_drop_db(db_name="tpcds"):
    sql = f"DROP DATABASE IF EXISTS {db_name}"
    return sql


def construct_create_db(db_name="tpcds"):
    sql = f"CREATE DATABASE IF NOT EXISTS {db_name}"
    return sql


def construct_create_schema(db_schema_file_path=None, file_name=None):
    try:
        full_db_schema_name = db_schema_file_path + file_name
        check_file_existence(full_db_schema_name)

        with open(full_db_schema_name, 'r') as file:
            data = file.read()

    except Exception as e:
        print(f"Error while construct_create_schema, error details: {e}")
    return construct_use_database() + data


def construct_use_database(db_name="tpcds"):
    sql = f"USE {db_name} ; \n"
    return sql


def load_data_into_table(data_parent_file_path, file_name, db_name="tpcds"):

    file_full_path = data_parent_file_path + file_name

    check_file_existence(file_full_path)

    # extract table name as file name like ali_test.dat, we need only ali_test
    table_name = file_name.split(".")[0]

    sql = f"LOAD DATA LOCAL INFILE '{file_full_path}' REPLACE INTO TABLE {db_name}.{table_name} FIELDS TERMINATED BY '|' LINES TERMINATED BY " + ''''\n';'''

    return sql
