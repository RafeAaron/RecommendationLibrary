# a filtering engine for the recommendation library

class FilteringEngine:
    def getCategories(self, data:dict):
        return data.keys()
    
    def getValuesForCategory(self, data:dict):
        return data.values()
    
    def getValuesForCategoryWithLabel(self, data:list, label, category):

        values = []

        for dataPoint in data:
            if category in dataPoint.keys() and label in dataPoint[category].keys():
                values.append(dataPoint.values())

        return values

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

        return values

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
    
    def sortRecords(self, data:list, labelToUse:str):

        dataSieved = []
        values = []
        highest = 0
        highestIndex = -1
        takenIndexes = []

        for dataPoint in data:
            if labelToUse in dataPoint.values().keys():
                dataSieved.append(dataPoint)

        for i in range(len(dataSieved)):
            highestIndex = 0
            for a in range(len(dataSieved)):
                if dataSieved[a].values()[labelToUse] > highest and a not in takenIndexes:
                    highest = dataSieved[a].values()[labelToUse]
                    highestIndex = a
                    takenIndexes.append(a)

            values.append(dataSieved[highestIndex])

                    
            