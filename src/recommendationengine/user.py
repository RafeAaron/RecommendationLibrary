#Users Class
from history import History
from location import Location
import json

class User:

    def __init__(self, id:str, history:History = None, location:Location = None):
        self.id = id

        if location is None:
            self.location = "Unknown"
        else:
            self.location = location

        if history is None:
            self.history:History = []
        else:
            self.history:History = history.getHistory()

    def addToHistory(self, data:list):
        self.history.addToHistory(data)

    def deleteFromHistory(self, id:str, category:str=None):
        self.history.deleteRecordHistory(id, category)

    def searchInHistory(self, id:str, category:str):
        self.history.searchForRecordInHistory(id, category)

    def getLocation(self):
        return self.location.getLocation()
    
    def setLocation(self, location:Location):
        self.location = location

    def objectToDict(self):
        return {"user": {"id": self.id, "history": self.history.objectToDict(), "location": self.getLocation()}}
    
    def toJSON(self):
        return json.dumps(self.objectToDict())
