import csv
import json
from PlayersDB.base_handler import BaseHandlerInterface
import os.path as op
from pprint import pp

class CSVHandler(BaseHandlerInterface):

    def __init__(self, path_to_file: str=""):
        super().__init__()
        self._file_path = path_to_file
        self._csv_data = None
        self.__update_json_data()
        self.__update_csv_data()

    def __update_csv_data(self):
        players_file = open(self._file_path, "r")
        self._csv_data = csv.reader(players_file)

    def __update_json_data(self):
        players_file = open(self._file_path, "r", encoding="utf8")
        json_data = csv.DictReader(players_file)
        data = {}

        # Convert each row into a dictionary
        # and add it to data
        for rows in json_data:
            # Assuming a column named 'No' to
            # be the primary key
            key = rows['Name']
            data[key] = rows

        # Open a json writer, and use the json.dumps()
        # function to dump data
        self._json_data = json.loads(json.dumps(data, indent=4))

    @property
    def csv_data(self) -> list:
        """Gets csv data of the playes.
        :return: csv data
        :rtype: list
        """
        return self._csv_data

    def delete_item(self, key : str=None) -> bool:
        deleted = False
        data = list()
        for row in self._csv_data:
            data.append(row)
            for field in row:
                if field.lower() == key.lower():
                    data.remove(row)
                    deleted = True
                    print("%s was deleted from the DB" %key)
        if deleted:
            with open(self._file_path, 'w', newline='') as writeFile:
                writer = csv.writer(writeFile)
                writer.writerows(data)
                writeFile.close()
            self.__update_json_data()
            self.__update_csv_data()
        return deleted

    def add_item(self, item : dict=None) ->  None:
        values = list(item.values())
        with open(self._file_path, 'a+', newline='') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerow(values)
            writeFile.close()
        self.__update_json_data()
        self.__update_csv_data()

if __name__ == "__main__":
    csv_file =  op.join(op.dirname(op.realpath(__file__)),"Players.csv")
    csv_handler = CSVHandler(csv_file)
    pp(csv_handler.json_data)