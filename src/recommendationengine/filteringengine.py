# a filtering engine for the recommendation library

class FilteringEngine:
    def getCategories(self, data:dict):
        return data.keys()
    
    def getValuesForCategory(self, data:dict):
        return data.values()
    
    def doesLabelExist(self, label, dataPresent:list):
        for data in dataPresent:
            if label not in data.keys():
                return False
            
            return True
        
    def getRecordsWithLabels(self, labels:list, data:list):

        values = []

        for label in labels:
            for dataValue in data:
                if label in dataValue.keys() and data not in values:
                    values.append(dataValue)

        return values
                    

    
    def getRecordsWithLabel(self, label, data:list):
        values = []

        for value in data:
            if label in value.keys():
                values.append(value)

        return values
    
    def getLabels(self, data:dict):
        values = []

        for data in data.keys():
            values.append(data)

    def getValuesWithSubstring(self, data:dict, substring:str):
        values = []
        
        for value in data.values():
            if value.find(substring) == -1:
                values.append(value)

        return values
    
    def getValuesGreaterThan(self, data:dict, base:int, fieldName:str):

        values = []

        for value in data.values():
            if value[fieldName] > base:
                values.append(value)

        return values
    
    def getValuesLessThan(self, data:dict, base:int, fieldName:str):

        values = []

        for value in data.values():
            if value[fieldName] < base:
                values.append(value)

        return values
    
    def getValuesEqualTo(self, data:dict, base:int, fieldName:str):

        values = []

        for value in data.values():
            if value[fieldName] == base:
                values.append(value)

        return values
    
    def getValuesLessThanOrEqualTo(self, data:dict, base:int, fieldName:str):

        values = []

        for value in data.values():
            if value[fieldName] <= base:
                values.append(value)

        return values
    
    def getValuesGreaterThanOrEqualTo(self, data:dict, base:int, fieldName:str):

        values = []

        for value in data.values():
            if value[fieldName] >= base:
                values.append(value)

        return values