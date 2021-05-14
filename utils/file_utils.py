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
                json.dump(data, file, indent=4)
        except FileNotFoundError as fnf:
            print(constant.ERROR_MESSAGES)
            return fnf
        except Exception as e:
            print(constant.ERROR_MESSAGES)
            return e

    @staticmethod
    def get_data(email: str) -> str:
        try:
            with open(constant.CUSTOMER_RESOURCES_PATH) as file:
                data = json.load(file)
                customers = data["customers"]
                for customer in customers:
                    if(customer["email"] == email):
                        return email
                return constant.EMPTY_STRING
        except FileNotFoundError as fnf:
            print(constant.ERROR_MESSAGES)
            return fnf
        except Exception as e:
            print(constant.ERROR_MESSAGES)
            raise
            return e
