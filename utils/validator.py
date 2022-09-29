from os.path import exists


def check_file_existence(file=None):
    if not file:
        raise Exception("Empty file name/path, you should provide the full file path and name")

# confirm if file exist
    file_exists = exists(file)
    if not file_exists:
        raise Exception(f"file {file} doesn't exist, or you have no permission to access it,"
                        f" please provide another one")