from configparser import ConfigParser
import os

# список id интересных компаний
employer_ids = [15478, 1272486, 4181, 3776, 4934, 39305, 49357, 2120, 816144, 1276]

JSON_DATA_DIR = os.path.join('data')
JSON_FILE_NAME = 'data.json'


def config(filename='database.ini', section='postgresql'):
    parser = ConfigParser()

    parser.read(filename)
    if parser.has_section(section):
        params = parser.items(section)
        db = dict(params)
    else:
        raise Exception("Раздел не найден")
    return db
