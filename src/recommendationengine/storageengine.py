# A storage engine for the data present within the system like movies, music and notifications
import json

class StorageEngine:
    def __init__(self, storageFileLocation = "Null"):
        self.data = {}

        if storageFileLocation == "Null":
            self.data = {}
        
        else:
            try:
                file = open(storageFileLocation, "r")
                self.data = json.loads(file.read())

            except IOError as ioerror:
                print(f"There was an error opening the file for reading. Error: {ioerror}")
                cwd = os.getcwd()  # Get the current working directory (cwd)
                files = os.listdir(cwd)  # Get all the files in that directory
                print("Files in the current directory are %s" % (files))

            except:
                print("There was an error initializing the Storage Engine")

    def getSavedData(self):
        return self.data
    
    def viewCategoriesOfStoredData(self):
        for keys in self.data:
            print(keys)

    def returnDataInCategory(self, category):
        values = []
        movieids = []

        if category not in self.data.keys():
            return "Category Doesn't Exist"
        
        for value in self.data[category]:
            movieids.append(value)

        for value in self.data[category].values():
            values.append(value)

        return values
    
    def loadData(self, storageLocation):
        try:

            file = open(storageLocation, "r")
            loadedData = json.loads(file.read())

            for category in loadedData.keys():
                if category not in self.data.keys():
                    self.data[category] = loadedData[category]

                else:
                    for example in loadedData[category].keys():
                        self.data[category][self.data[category][example]]  =loadedData[category][example]


        except IOError as ioError:
            print(f"Error: {ioError}")

    def saveData(self, saveLocation):
        try:
            file = open(saveLocation, "w")
            
            saveddata = json.dumps(self.data)

            file.write(saveddata)

            file.close()

        except IOError as ioErr:
            return ioErr
        
    def doesCategoryExist(self, category) -> bool:
        if category in self.data.keys():
            return True
        
        else:
            return False
        
    def doesRecordExist(self, label):
        for value in self.data.keys():
            for subvalue in value[value].keys():
                if label == subvalue:
                    return label
                
            
        return False