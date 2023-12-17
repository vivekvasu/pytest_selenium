import json

class File_Reader:

    @staticmethod
    def read_json(path:str):
        try:
            file = open(path)
            return json.load(file)
        finally:
                file.close()

