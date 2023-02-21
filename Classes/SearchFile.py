import csv
from Classes.InitValues import InitValues as iv

class SearchFile():
    
    def searchFile(self, select_file, search_field: str, search_value: str) -> list:
        with open(select_file, mode='r', encoding='utf-8') as fh:
            reader = csv.DictReader(fh)
            dict_list = list(reader)
        
        fdict_list = []
        for item in dict_list:
            for key, value in item.items():
                if key == search_field and value == search_value:
                    fdict_list.append(item)
                # elif key == 'REQUIRED PRICE TO AMAZON' and value == float(search_value):
                #     fdict_list.append(item)
                else:
                    continue
        return fdict_list

        pass