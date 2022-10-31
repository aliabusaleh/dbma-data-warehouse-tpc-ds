# BDMA Data Warehouse
<hr>

This project is done under the BDMA first semester at Université Libre de Bruxelles

## Overview
<hr>

TPC-DS is a decision support benchmark that models several generally 
applicable aspects of a decision support system, including queries 
and data maintenance.

This project is done by: <br />
* <b>[Ali AbuSaleh](https://github.com/aliabusaleh)
* [Muhammad Rizwan Khalid](https://github.com/mrizwank97)
* [Aliakberova, Liliia](https://github.com/Liliia-Aliakberova)
* [Mayorga Llano, Mariana](https://github.com/marianamllano) </b> <br/>

 Under supervision of professor <b>Esteban Zimanyi</b>


## Technology and tools used in this project
<hr>

we selected <b>MySQL</b> 
Database technology to implement and test the TPC-DS. 


# Setup and Tools

<hr>

## Tools setup 
 <hr> 

### MySQL setup
In order to run this project, you need to install [MySQL V8.0](https://dev.mysql.com/doc/refman/8.0/en/installing.html) 
and also [Python V3.x](https://www.python.org/downloads/) on your machine.

<sub>**_Note_**:  Python scripts done's support parallel programming, 
and it's good to "weak" machines (local use) <b> use scale factor of 1</b>, 
but for cloud solution please use the bash scripts<br> </sub>


<hr> 

## Scripts Description
### [Util](/utils): 
#### &nbsp;&nbsp;&nbsp;&nbsp;[File_modification.py](/utils/file_modifications.py) 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; which is a script to handle the null values in the generated data, since the 
generated data has special characters ("||") for null values, this 
script will replace the null values ("||") with ("\N") which suit MySQL 
to read the value as null.

#### &nbsp;&nbsp;&nbsp;&nbsp;[Query Generator.py](/utils/query_generator.py) 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; This script will handle the
generation for the queries, such as create DB, drop DB, create load
statements in order to execute it in later step.... etc.

#### &nbsp;&nbsp;&nbsp;&nbsp;[Validator.py](/utils/validator.py) 

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; This script will check the existence of a file in ur system.

### MySQL Class
This class is the main class to connect to my MySQL server and execute the SQLs.


### Requirements
The dependencies of the project.

<hr>

## How to run the project
1. Generate the data using TPC tool
2. You need to add the following local variables(export in case of shell):  
   1. Schema root directory ->  *DB_SCHEMA_PATH*
   2. Schema file name (.SQL) -> *DB_SCHEMA_FILE_NAME*
   3. Generated data root path -> *DATA_ROOT_PATH*
   4. DB info
      1. host -> *DB_HOST* 
      2. port -> *DB_PORT* 
      3. username -> *DB_USERNAME*
      4. password -> *DB_PASSWORD* 
5. Run main.py 
6. Check the loaded Data and the created schema
7. Generate the Queries (using TPC tool)
8. Modify *mysql_execute_queries.sh* with your correct directory of the queries
9. Modify *mysql_execute_query.sh* with correct USERNAME and PASSWORD for mysql
10. RUN *mysql_execute_queries.sh* "usage described in the comment inside the file"
11. When Step 8 is done, run *mysql_result_summary.sh* 

<u>All Bash scripts has usage description on the files.</u>

[//]: <> (more info to be added)
