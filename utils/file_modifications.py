from utils.validator import check_file_existence


def handle_null_values(file, encoding='latin-1'):
    try:
        check_file_existence(file)
        # read file content line by line
        f = open(file, 'r', encoding=encoding)
        linelist = f.readlines()
        f.close()

        # Re-open file here to modify it
        f2 = open(file, 'w')
        for line in linelist:
            line = "\\N" + line if line[0] == "|" else line
            line = line.replace("||||||||||", "|\\N|\\N|\\N|\\N|\\N|\\N|\\N|\\N|\\N|")
            line = line.replace("|||||||||", "|\\N|\\N|\\N|\\N|\\N|\\N|\\N|\\N|")
            line = line.replace("||||||||", "|\\N|\\N|\\N|\\N|\\N|\\N|\\N|")
            line = line.replace("|||||||", "|\\N|\\N|\\N|\\N|\\N|\\N|")
            line = line.replace("||||||", "|\\N|\\N|\\N|\\N|\\N|")
            line = line.replace("|||||", "|\\N|\\N|\\N|\\N|")
            line = line.replace("||||", "|\\N|\\N|\\N|")
            line = line.replace("|||", "|\\N|\\N|")
            line = line.replace("||", "|\\N|")
            f2.write(line)
        f2.close()

    except Exception as e:
        print(f"Error while modifying file {file}, with error details: {e}")
