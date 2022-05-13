import csv
import json
from base_handler import BaseHandlerInterface

class CSVHandler(BaseHandlerInterface):

    def __init__(self, path_to_file: str="Players.csv"):
        self._file_path = path_to_file
        players_file = open(self._file_path, "r")
        self._csv_data = csv.reader(players_file)

    @property
    def get_data(self) -> list:
        """Gets csv data of the playes.


        :return: csv data
        :rtype: list
        """
        # players_file = open(self._file_path, "r", encoding="utf8")
        # self._csv_data = csv.reader(players_file)
        return self._csv_data

    def get_json(self) -> dict:
        # create a dictionary
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
        json_data = json.dumps(data, indent=4)
        return json_data

    def delete_item(self, key : str=None) -> bool:
        deleted = False
        data = list()
        for row in self._csv_data:
            data.append(row)
            for field in row:
                if field.lower() == key.lower():
                    data.remove(row)
                    deleted = True
        with open(self._file_path, 'w', newline='') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(data)
            writeFile.close()
        return deleted

    def add_item(self, item : list=None) ->  None:
        with open(self._file_path, 'a+', newline='') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerow(row)
            writeFile.close()

if __name__ == "__main__":
    csv_handler = CSVHandler()
    #csv_handler.delete_item("raz")
    csv_handler.add_item(['test', 1.1, 'Attack', 'X'])
    print ("DONE")
    print (csv_handler.get_json())