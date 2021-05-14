import json
from constants import constant

class FileUltils:
    @staticmethod
    def write_data(model: dict, path: str):
        try:
            with open(path) as file:
                data = json.load(file)
                temp = data["customers"]
                temp.append(model)
            with open(path, "w") as file:
                json.dump(data, file, indent = 4)
        except FileNotFoundError as fnf:
            print("Some thing went wrong, please contact to admin!")
            return fnf
        except Exception as e:
            print("Some thing went wrong, please contact to admin!")
            return e
